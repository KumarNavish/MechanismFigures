"""One-off, reviewable root-layout migration on the isolated work branch only."""
from pathlib import Path
import hashlib,json,shutil,subprocess
R=Path(__file__).resolve().parents[2]
bundle=json.loads((Path(__file__).parent/'rewrites.json').read_text())
old=R/'skills/mechanism-figures'
if not (old/'SKILL.md').is_file():raise SystemExit('Expected unmigrated source tree; refusing replay')
# Merge the old canonical payload with the new support files already on this branch.
for source in sorted(old.rglob('*')):
    if not source.is_file():continue
    rel=source.relative_to(old);target=R/rel
    if target.exists():
        if rel.as_posix() not in {'LICENSE','THIRD_PARTY.md'} or target.read_bytes()!=source.read_bytes():
            raise SystemExit('Unexpected root collision: '+str(rel))
        source.unlink()
    else:
        target.parent.mkdir(parents=True,exist_ok=True);shutil.move(str(source),str(target))
for directory in sorted([p for p in old.rglob('*') if p.is_dir()],key=lambda p:len(p.parts),reverse=True):directory.rmdir()
old.rmdir()
for patch in bundle['patches']:
    rel=Path(patch['path'])
    if rel.is_absolute() or '..' in rel.parts:raise SystemExit('Invalid patch path')
    target=R/rel;data=target.read_bytes()
    if hashlib.sha256(data).hexdigest()!=patch['before']:raise SystemExit('Source changed: '+str(rel))
    text=data.decode()
    for edit in reversed(patch['edits']):
        i,j=edit['start'],edit['end']
        if text[i:j]!=edit['old']:raise SystemExit('Patch precondition failed: '+str(rel))
        text=text[:i]+edit['new']+text[j:]
    if hashlib.sha256(text.encode()).hexdigest()!=patch['after']:raise SystemExit('Patch output differs: '+str(rel))
    target.write_text(text)
for name,text in bundle['compatibility'].items():
    rel=Path(name)
    if rel.parts[:3]!=('skills','mechanism-figures','assets') or rel.name not in {'gallery.html','motion.html'}:raise SystemExit('Invalid compatibility target')
    target=R/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(text)
for name in ['.agents/plugins/marketplace.json','.github/workflows/source-snapshot.yml']:
    p=R/name
    if not p.is_file():raise SystemExit('Expected retired metadata: '+name)
    p.unlink()
# Reuse the frozen public diagnostic packet; no new model-generated evidence.
tasks=json.loads((R/'benchmarks/tasks.json').read_text())['tasks'];evals=[]
for t in tasks:
    evals.append({'id':t['id'],'prompt':'Use mechanism-figures. '+t['mechanism'],'context':t['project_context'],'evidence':t['available_evidence'],'constraints':t['output_constraints'],'expected':['Inspect two actual current reference images and record their concrete visual operation.','Map actual evidence to persistent entities, interfaces and state; do not add unsupported causal claims.','Deliver editable vector, final-size preview, caption, source and version-bound review; inspect 4x details.'],'must_not':['Replace scientific evidence with an analogy.','Use retired or self-generated calibration images.','Claim an independent review or achieved score without a real record.']})
(R/'evals').mkdir(exist_ok=True)
(R/'evals/evals.json').write_text(json.dumps({'schema_version':1,'status':'Public diagnostic tasks; not an efficacy study or held-out benchmark.','evals':evals},indent=2)+'\n')
# The temporary migration mechanism does not become part of the product.
for name in ['.github/migrations/rewrites.json','.github/migrations/root-layout.py','.github/workflows/root-migration.yml']:
    (R/name).unlink()
subprocess.run(['python3','tools/build_gallery.py'],cwd=R,check=True)
subprocess.run(['python3','-m','unittest','discover','-s','tests','-q'],cwd=R,check=True)
subprocess.run(['python3','tools/check_repo.py'],cwd=R,check=True)
print('Verified migration complete; no reference pixels or external user installation changed.')
