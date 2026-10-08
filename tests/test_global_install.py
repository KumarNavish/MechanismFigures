"""Global setup is a file transaction, never a model invocation or cloud-install claim."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
from global_install import apply, doctor, plan, recover, disk_state, PROFILES
from install import MARKER


class GlobalInstallTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.base=Path(self.temp.name);self.home=self.base/'user';self.home.mkdir()
        self.source=self.base/'source';self.source.mkdir();(self.source/'SKILL.md').write_text('---\nname: mechanism-figures\ndescription: Test only\n---\nTest fixture.\n');(self.source/'payload.txt').write_text('v1')
    def tearDown(self):self.temp.cleanup()
    def install(self,**kw):return apply(self.home,source=self.source,**kw)
    def check(self):return doctor(self.home,source=self.source)
    def test_all_eight_routes_use_one_canonical_and_two_adapters(self):
        result=self.install();self.assertTrue(result['accepted']);self.assertEqual(len(result['hosts']),8)
        self.assertTrue(all(h['files_verified'] for h in result['hosts']))
        self.assertEqual(sum(h['storage']=='link' for h in result['hosts']),2)
        for h in result['hosts']:self.assertEqual(h['runtime_activation'],'not_tested_no_agent_invoked')
    def test_install_is_idempotent(self):
        self.install();r=self.install();self.assertEqual(r['status'],'already_installed');self.assertEqual(r['changed_targets'],[])
    def test_dry_run_writes_nothing(self):
        before=list(self.home.rglob('*'));r=self.install(dry_run=True);self.assertEqual(r['status'],'planned');self.assertEqual(list(self.home.rglob('*')),before)
    def test_doctor_is_read_only(self):
        r=self.check();self.assertFalse(r['accepted']);self.assertEqual(list(self.home.iterdir()),[])
    def test_unknown_agent_is_not_invented(self):
        with self.assertRaises(ValueError):self.install(agents='unlisted-agent')
    def test_unmanaged_adapter_blocks_before_canonical_change(self):
        p=self.home/'.claude/skills/mechanism-figures';p.mkdir(parents=True);(p/'mine').write_text('keep')
        r=self.install();self.assertFalse(r['accepted']);self.assertFalse((self.home/'.agents/skills/mechanism-figures').exists());self.assertEqual((p/'mine').read_text(),'keep')
    def test_modified_canonical_blocks_update(self):
        self.install();p=self.home/'.agents/skills/mechanism-figures/payload.txt';p.write_text('user edit');(self.source/'payload.txt').write_text('v2')
        r=self.install(update=True);self.assertFalse(r['accepted']);self.assertEqual(p.read_text(),'user edit')
    def test_unrelated_global_prompts_preserved(self):
        for name in ['.codex/AGENTS.md','.claude/CLAUDE.md','.gemini/GEMINI.md']:
            p=self.home/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('existing user policy '+name)
        self.install()
        for name in ['.codex/AGENTS.md','.claude/CLAUDE.md','.gemini/GEMINI.md']:self.assertEqual((self.home/name).read_text(),'existing user policy '+name)
    def test_update_requires_explicit_flag(self):
        self.install();(self.source/'payload.txt').write_text('v2');r=self.install();self.assertFalse(r['accepted'])
        self.assertEqual((self.home/'.agents/skills/mechanism-figures/payload.txt').read_text(),'v1')
    def test_update_preserves_old_version_and_updates_alias_views(self):
        self.install();(self.source/'payload.txt').write_text('v2');r=self.install(update=True);self.assertTrue(r['accepted'])
        self.assertEqual((self.home/'.claude/skills/mechanism-figures/payload.txt').read_text(),'v2')
        old=list((self.home/'.agents/mechanism-figures-state/backups').glob('*/canonical/payload.txt'));self.assertTrue(any(p.read_text()=='v1' for p in old))
    def test_copy_adapter_updates_when_later_selection_is_smaller(self):
        self.install(mode='copy');(self.source/'payload.txt').write_text('v2');r=self.install(agents='codex',update=True)
        self.assertTrue(r['accepted']);self.assertEqual((self.home/'.claude/skills/mechanism-figures/payload.txt').read_text(),'v2')
        self.assertEqual((self.home/'.codeium/windsurf/skills/mechanism-figures/payload.txt').read_text(),'v2')
    def test_wrong_existing_symlink_is_not_replaced(self):
        other=self.home/'unrelated';other.mkdir();p=self.home/'.claude/skills/mechanism-figures';p.parent.mkdir(parents=True);p.symlink_to(other,target_is_directory=True)
        r=self.install();self.assertFalse(r['accepted']);self.assertEqual(p.resolve(),other.resolve())
    def test_symlink_parent_refuses_writes(self):
        other=self.base/'outside';other.mkdir();(self.home/'.agents').symlink_to(other,target_is_directory=True)
        with self.assertRaises(ValueError):self.install()
        self.assertEqual(list(other.iterdir()),[])
    def test_failure_rolls_back_new_installation(self):
        with self.assertRaises(RuntimeError):self.install(_fail_after=0)
        self.assertFalse((self.home/'.agents/skills/mechanism-figures').exists())
        self.assertFalse((self.home/'.claude/skills/mechanism-figures').exists())
        self.assertEqual(recover(self.home)['status'],'nothing_to_recover')
    def test_failure_rolls_back_upgrade_and_keeps_adapters(self):
        self.install();(self.source/'payload.txt').write_text('v2')
        with self.assertRaises(RuntimeError):self.install(update=True,_fail_after=0)
        self.assertEqual((self.home/'.agents/skills/mechanism-figures/payload.txt').read_text(),'v1')
        self.assertEqual((self.home/'.claude/skills/mechanism-figures/payload.txt').read_text(),'v1')
    def test_recovery_will_not_remove_user_changed_target(self):
        self.install();state=self.home/'.agents/mechanism-figures-state';j=json.loads((state/'transaction.json').read_text());j['status']='prepared';j['pid']=None;(state/'transaction.json').write_text(json.dumps(j))
        p=self.home/'.agents/skills/mechanism-figures/payload.txt';p.write_text('post-failure edit')
        with self.assertRaises(ValueError):recover(self.home)
        self.assertEqual(p.read_text(),'post-failure edit')
    def test_scope_and_account_limits_are_explicit(self):
        r=self.install();self.assertIn('operating-system user',r['scope']);self.assertIn('not_tested',r['hosts'][0]['runtime_activation'])
        self.assertTrue(any(x['status']=='package_ready_not_directory_published' for x in r['account_surfaces']))
    def test_interrupted_new_install_can_be_reconciled(self):
        self.install();state=self.home/'.agents/mechanism-figures-state';jp=state/'transaction.json';j=json.loads(jp.read_text());j['status']='prepared';j['pid']=None;jp.write_text(json.dumps(j))
        self.assertEqual(recover(self.home)['status'],'recovered_previous_installation')
        self.assertFalse((self.home/'.agents/skills/mechanism-figures').exists());self.assertFalse((state/'installed.json').exists())
    def test_interrupted_update_restores_previous_receipt_and_files(self):
        self.install();state=self.home/'.agents/mechanism-figures-state';previous=json.loads((state/'installed.json').read_text());(self.source/'payload.txt').write_text('v2');self.install(update=True)
        jp=state/'transaction.json';j=json.loads(jp.read_text());j['status']='prepared';j['pid']=None;jp.write_text(json.dumps(j));recover(self.home)
        self.assertEqual(json.loads((state/'installed.json').read_text()),previous)
        self.assertEqual((self.home/'.agents/skills/mechanism-figures/payload.txt').read_text(),'v1')
    def test_doctor_reports_an_outstanding_lock(self):
        self.install();state=self.home/'.agents/mechanism-figures-state';(state/'install.lock').write_text('12345')
        self.assertTrue(self.check()['pending_transaction']);self.assertFalse(self.check()['accepted'])
    def test_state_directory_symlink_is_refused(self):
        outside=self.base/'external-state';outside.mkdir();state=self.home/'.agents/mechanism-figures-state';state.parent.mkdir();state.symlink_to(outside,target_is_directory=True)
        with self.assertRaises(ValueError):self.install()
        self.assertEqual(list(outside.iterdir()),[])
    def test_dry_run_keeps_hash_inventory_out_of_agent_context(self):
        self.install();r=self.install(dry_run=True)
        self.assertTrue(r['accepted'])
        canonical=r['targets'][0]['before']
        self.assertNotIn('files',canonical);self.assertEqual(canonical['file_count'],2)
        self.assertEqual(len(canonical['inventory_sha256']),64)
    def test_root_help_does_not_import_a_model_runner(self):
        s=(ROOT/'tools/global_install.py').read_text();self.assertNotIn('subprocess',s);self.assertNotIn('os.system',s)
    def test_portable_plugin_and_local_catalog_are_not_auto_enabled(self):
        p=json.loads((ROOT/'plugin.json').read_text());self.assertEqual(p['name'],'mechanism-figures');self.assertEqual(p['version'],'0.4.0')
        m=json.loads((ROOT/'.agents/plugins/marketplace.json').read_text());self.assertEqual(m['plugins'][0]['source']['path'],'./');self.assertEqual(m['plugins'][0]['policy']['installation'],'AVAILABLE')


if __name__=='__main__':unittest.main()
