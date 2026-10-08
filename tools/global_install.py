"""User-scoped, multi-host skill installation. No agent process or account setting is touched."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import uuid

from install import SOURCE, NAME, MARKER, inventory

ROOT = Path(__file__).resolve().parents[1]
VERSION = '0.4.0'
PROFILES = json.loads((Path(__file__).parent/'agent_hosts.json').read_text())


def atomic_json(path, value):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+'.pending')
    with temp.open('w', encoding='utf-8') as out:
        json.dump(value, out, indent=2, ensure_ascii=False); out.write('\n');out.flush();os.fsync(out.fileno())
    temp.replace(path)


def under_home(home, relative):
    rel=Path(relative)
    if rel.is_absolute() or '..' in rel.parts: raise ValueError('Expected a contained user-relative path')
    path=home/rel; cursor=home
    for part in rel.parts[:-1]:
        cursor=cursor/part
        if cursor.is_symlink(): raise ValueError('A parent is a symlink; inspect it before installing: '+str(cursor))
    return path


def disk_state(path):
    path=Path(path)
    if path.is_symlink(): return {'kind':'link','to':str(path.resolve(strict=False))}
    if not path.exists(): return {'kind':'absent'}
    if not path.is_dir(): return {'kind':'conflict','reason':'not a directory'}
    marker=path/MARKER
    if not marker.is_file() or marker.is_symlink():return {'kind':'conflict','reason':'unmanaged directory'}
    try:
        data=json.loads(marker.read_text());actual=inventory(path)
    except (OSError,ValueError) as exc:return {'kind':'conflict','reason':str(exc)}
    if data.get('files')!=actual:return {'kind':'conflict','reason':'managed files have local changes'}
    return {'kind':'tree','files':actual,'version':data.get('version')}


def selected_hosts(agents):
    ids={h['id'] for h in PROFILES['hosts']}
    selected=ids if agents=='all' else set(agents.split(','))
    if not selected or not selected.issubset(ids):raise ValueError('Unknown agent. Supported: '+', '.join(sorted(ids)))
    return [h for h in PROFILES['hosts'] if h['id'] in selected]


def paths_for(home):
    home=Path(home).expanduser().absolute()
    if home.is_symlink():raise ValueError('Resolve the home-directory symlink explicitly before installation')
    home=home.resolve()  # normalize OS-level parents such as macOS /var -> /private/var
    state=under_home(home,'.agents/mechanism-figures-state')
    if state.is_symlink():raise ValueError('Installation state must not be a symlink; inspect it before installing')
    for name in ['staging','backups','installed.json','transaction.json','install.lock']:
        if (state/name).is_symlink():raise ValueError('Managed installation state contains a symlink: '+name)
    canonical=under_home(home,PROFILES['canonical'])
    return home,state,canonical


def plan(home, agents='all', update=False, mode='auto', source=SOURCE):
    home,state,canonical=paths_for(home)
    if mode not in {'auto','link','copy'}:raise ValueError('Adapter mode must be auto, link or copy')
    source=Path(source).resolve();expected=inventory(source)
    if 'SKILL.md' not in expected:raise ValueError('Source skill is incomplete')
    targets=[{'path':str(canonical),'role':'canonical','desired':'tree'}]
    hosts=selected_hosts(agents)
    for h in hosts:
        p=under_home(home,h['directory']+'/'+NAME)
        if p==canonical:continue
        targets.append({'path':str(p),'role':h['id'],'desired':'copy' if mode=='copy' else 'link'})
    # Include previously managed adapters when updating, even when fewer hosts were selected.
    receipt=state/'installed.json'
    if receipt.exists():
        saved=json.loads(receipt.read_text())
        for old in saved.get('targets',[]):
            p=Path(old['path'])
            try:rel=p.relative_to(home)
            except ValueError:raise ValueError('Saved adapter escaped the user home')
            allowed={h['directory']+'/'+NAME for h in PROFILES['hosts']}|{PROFILES['canonical']}
            if rel.as_posix() not in allowed:raise ValueError('Unknown saved target; reconcile before update')
            if str(p) not in {t['path'] for t in targets}:
                targets.append({'path':str(p),'role':old['role'],'desired':old['desired']})
    conflicts=[];changes=[]
    for t in targets:
        p=Path(t['path']);current=disk_state(p);t['before']=current
        if current['kind']=='conflict':conflicts.append(str(p)+': '+current['reason']);continue
        if p==canonical and current['kind']=='link':conflicts.append(str(p)+': canonical directory must not be a symlink');continue
        if current['kind']=='link':
            if current['to']!=str(canonical):conflicts.append(str(p)+': link belongs to another installation')
            else:t['desired']='link';t['change']=False
            continue
        if current['kind']=='tree' and current['files']!=expected and not update:
            conflicts.append(str(p)+': older/different managed version; use --update after review');continue
        if p!=canonical and current['kind']=='tree':t['desired']='copy' # preserve explicit copy strategy
        t['change']=current['kind']=='absent' or (current['kind']=='tree' and current['files']!=expected)
        if t['change']:changes.append(t['path'])
    return {'home':str(home),'state_root':str(state),'canonical':str(canonical),'version':VERSION,'source':str(source),'expected':expected,'targets':targets,'selected_agents':[h['id'] for h in hosts],'adapter_mode':mode,'changes':changes,'conflicts':conflicts,'scope':PROFILES['scope']}


def build_tree(source, dest, expected):
    shutil.copytree(source,dest,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.DS_Store',MARKER))
    if inventory(dest)!=expected:raise ValueError('Staged copy does not match source')
    atomic_json(dest/MARKER,{'schema_version':1,'version':VERSION,'files':expected})


def owned_remove(path, expected):
    """Remove only an exact, verified staged installation during rollback."""
    p=Path(path)
    if disk_state(p)!=expected:raise ValueError('Refusing to remove a changed rollback target: '+str(p))
    if p.is_symlink():p.unlink()
    elif p.is_dir():shutil.rmtree(p)


def recover(home):
    home,state,canonical=paths_for(home);journal=state/'transaction.json';lock=state/'install.lock'
    if not journal.exists():
        if lock.exists():raise ValueError('Lock exists without a journal; inspect its process/receipt before removing it')
        return {'status':'nothing_to_recover'}
    j=json.loads(journal.read_text())
    if j.get('status') in {'committed','rolled_back'}:
        if lock.exists():raise ValueError('Final journal has a lock; inspect for a concurrent process')
        return {'status':'nothing_to_recover','previous_transaction':j['id']}
    pid=j.get('pid')
    if pid and pid!=os.getpid():
        try:os.kill(pid,0)
        except ProcessLookupError:pass
        except PermissionError:raise ValueError('Original installer may still be running')
        else:raise ValueError('Original installer PID still exists; do not replay its mutations')
    allowed={str(home/h['directory']/NAME) for h in PROFILES['hosts']}|{str(canonical)}
    # Validate all possible reversals first; never overwrite a post-interruption user edit.
    for item in j['operations']:
        target=Path(item['target']);backup=Path(item['backup'])
        if str(target) not in allowed:raise ValueError('Unrecognized recovery target')
        try:backup.relative_to(state/'backups')
        except ValueError:raise ValueError('Unrecognized recovery backup')
        current=disk_state(target)
        if current not in [item['before'],item['after'],{'kind':'absent'}]:raise ValueError('Recovery target changed externally: '+str(target))
        if backup.exists() and disk_state(backup)!=item['before']:raise ValueError('Recovery backup changed externally')
    for item in reversed(j['operations']):
        target=Path(item['target']);backup=Path(item['backup']);current=disk_state(target)
        if current==item['after']:owned_remove(target,current)
        if backup.exists():
            if target.exists() or target.is_symlink():raise ValueError('Recovery destination unexpectedly occupied')
            backup.rename(target)
    receipt=state/'installed.json'
    if receipt.exists() and json.loads(receipt.read_text()).get('transaction')==j['id']:
        if j.get('previous_receipt') is None:receipt.unlink()
        else:atomic_json(receipt,j['previous_receipt'])
    j['status']='rolled_back';atomic_json(journal,j)
    if lock.exists():lock.unlink()
    return {'status':'recovered_previous_installation','transaction':j['id'],'note':'Only exact managed targets were reversed; backups and transaction record are retained.'}


def apply(home,agents='all',update=False,mode='auto',source=SOURCE,dry_run=False,_fail_after=None):
    p=plan(home,agents,update,mode,source)
    public={k:v for k,v in p.items() if k not in {'expected','source','targets'}}
    public['targets']=[]
    for target in p['targets']:
        visible={k:v for k,v in target.items() if k!='before'}
        before={k:v for k,v in target['before'].items() if k!='files'}
        if 'files' in target['before']:
            files=target['before']['files']
            before.update(file_count=len(files),inventory_sha256=hashlib.sha256(json.dumps(files,sort_keys=True).encode()).hexdigest())
        visible['before']=before;public['targets'].append(visible)
    if p['conflicts']:return {'status':'conflict','accepted':False,**public}
    if dry_run:return {'status':'planned','accepted':True,**public}
    home,state,canonical=paths_for(home)
    journal=state/'transaction.json'
    if journal.exists() and json.loads(journal.read_text()).get('status') not in {'committed','rolled_back'}:
        raise ValueError('An interrupted transaction exists. Run --recover before another mutation.')
    state.mkdir(parents=True,exist_ok=True)
    lock=state/'install.lock'
    fd=os.open(str(lock),os.O_CREAT|os.O_EXCL|os.O_WRONLY,0o600)
    os.write(fd,(str(os.getpid())+'\n').encode());os.close(fd)
    tx=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S')+'-'+uuid.uuid4().hex[:8]
    staging=state/'staging'/tx;backup_root=state/'backups'/tx
    staging.mkdir(parents=True);backup_root.mkdir(parents=True)
    operations=[]
    try:
        # Revalidate after taking the exclusive installation lock.
        for t in p['targets']:
            if disk_state(t['path'])!=t['before']:raise ValueError('Target changed since preflight: '+t['path'])
            if not t.get('change'):continue
            staged=staging/t['role'];target=Path(t['path'])
            if t['desired']=='link':
                try:staged.symlink_to(canonical,target_is_directory=True)
                except OSError:
                    if mode=='link':raise
                    build_tree(p['source'],staged,p['expected']);t['desired']='copy'
            else:build_tree(p['source'],staged,p['expected'])
            after=disk_state(staged)
            operations.append({'target':str(target),'staged':str(staged),'backup':str(backup_root/t['role']),'before':t['before'],'after':after})
        j={'id':tx,'pid':os.getpid(),'status':'prepared','version':VERSION,'operations':operations,'previous_receipt':json.loads((state/'installed.json').read_text()) if (state/'installed.json').exists() else None}
        atomic_json(journal,j)
        for n,item in enumerate(operations):
            target=Path(item['target']);target.parent.mkdir(parents=True,exist_ok=True)
            if disk_state(target)!=item['before']:raise ValueError('Target changed during staging: '+str(target))
            if target.exists() or target.is_symlink():target.rename(item['backup'])
            Path(item['staged']).rename(target)
            if _fail_after==n:raise RuntimeError('Injected transaction failure for regression test')
        targets=[{k:t[k] for k in ['path','role','desired']} for t in p['targets']]
        receipt={'schema_version':1,'transaction':tx,'version':VERSION,'canonical':str(canonical),'targets':targets,'selected_agents':p['selected_agents'],'scope':PROFILES['scope']}
        atomic_json(state/'installed.json',receipt)
        j['status']='committed';atomic_json(journal,j)
        lock.unlink()
        result=doctor(home,agents,source)
        result.update(status='installed' if operations else 'already_installed',transaction=tx,changed_targets=[o['target'] for o in operations],previous_versions_preserved=True)
        return result
    except BaseException:
        # Normal exceptions are immediately reversed. A killed process leaves the journal for --recover.
        if journal.exists() and json.loads(journal.read_text()).get('id')==tx:
            try:recover(home)
            except Exception:pass # never hide original failure; journal remains recoverable
        elif lock.exists():lock.unlink()
        raise


def doctor(home,agents='all',source=SOURCE):
    home,state,canonical=paths_for(home);expected=inventory(source);base=disk_state(canonical)
    base_ok=base.get('kind')=='tree' and base.get('files')==expected
    results=[]
    for host in selected_hosts(agents):
        p=under_home(home,host['directory']+'/'+NAME);actual=disk_state(p)
        good=base_ok and ((actual.get('kind')=='link' and actual.get('to')==str(canonical)) or (actual.get('kind')=='tree' and actual.get('files')==expected))
        results.append({'id':host['id'],'host':host['name'],'path':str(p),'files_verified':good,'storage':actual['kind'],'invoke':host['invoke'],'scope_limit':host['limit'],'runtime_activation':'not_tested_no_agent_invoked'})
    pending=(state/'install.lock').exists()
    if (state/'transaction.json').exists():pending=pending or json.loads((state/'transaction.json').read_text()).get('status') not in {'committed','rolled_back'}
    return {'status':'files_verified' if all(h['files_verified'] for h in results) and not pending else 'needs_attention','accepted':all(h['files_verified'] for h in results) and not pending,'version':VERSION,'canonical':str(canonical),'shared_file_count':len(expected),'hosts':results,'pending_transaction':pending,'account_surfaces':PROFILES['account_surfaces'],'scope':PROFILES['scope'],'next':'Refresh or restart the host, select this skill once, and inspect its real reference images. A local file check does not prove host activation or account-wide installation.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--global',dest='global_scope',action='store_true',help='User-global scope across local projects; this is the default')
    parser.add_argument('--agents',default='all',help='all, or comma-separated documented host IDs')
    parser.add_argument('--home',type=Path,default=Path.home(),help='Alternative user home, primarily for isolated tests')
    parser.add_argument('--adapter-mode',choices=['auto','link','copy'],default='auto')
    actions=parser.add_mutually_exclusive_group()
    actions.add_argument('--doctor',action='store_true',help='Read-only file and host-route verification')
    actions.add_argument('--update',action='store_true',help='Upgrade exact managed installations, retaining old versions')
    actions.add_argument('--recover',action='store_true',help='Roll back an interrupted owned transaction after checking actual state')
    parser.add_argument('--dry-run',action='store_true',help='Plan and detect conflicts without writing anything')
    args=parser.parse_args(argv)
    try:
        if args.recover:
            if args.dry_run:raise ValueError('--recover and --dry-run are separate operations')
            result=recover(args.home)
        elif args.doctor:result=doctor(args.home,args.agents)
        else:result=apply(args.home,args.agents,args.update,args.adapter_mode,dry_run=args.dry_run)
        print(json.dumps(result,indent=2,ensure_ascii=False))
        return 0 if result.get('accepted',True) else 2
    except (OSError,ValueError,RuntimeError) as exc:
        print(json.dumps({'status':'not_applied_or_needs_recovery','error':str(exc),'next':'Inspect --doctor and the retained transaction before retrying. No agent/account permissions were changed.'},indent=2));return 2


if __name__=='__main__':sys.exit(main())
