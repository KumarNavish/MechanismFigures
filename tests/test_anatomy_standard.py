"""Standard distribution and bounded construction checks; not visual-quality evidence."""
import importlib.util
import json
import math
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(ROOT/'tools'))
from kit import Scene,project,fit,transform
from install import inventory,copy_payload


class RootSkillTests(unittest.TestCase):
    def test_single_root_skill(self):
        skills=[p.relative_to(ROOT).as_posix() for p in ROOT.rglob('SKILL.md') if not any(part in {'.git','.work','.build'} for part in p.relative_to(ROOT).parts)]
        self.assertEqual(skills,['SKILL.md'])
    def test_standard_directories_and_entry_links(self):
        for name in ['kit','scripts','references','assets','agents','evals']:
            self.assertTrue((ROOT/name).is_dir())
        s=(ROOT/'SKILL.md').read_text()
        for name in ['craft.md','kit.md','verify.md','motion.md']:self.assertIn('references/'+name,s)
    def test_no_reference_images_added_or_replaced(self):
        d=json.loads((ROOT/'assets/calibration.json').read_text())
        self.assertEqual(len(d['references']),20);self.assertEqual(sum(len(r['assets']) for r in d['references']),29)
    def test_install_payload_excludes_private_work_and_git(self):
        names=inventory(ROOT)
        self.assertTrue({'SKILL.md','kit/scene.py','scripts/capture.mjs','references/craft.md'}.issubset(names))
        self.assertFalse(any(n.startswith(('.git/','.work/','.build/','skills/')) for n in names))
    def test_old_public_urls_redirect_without_duplicate_skill(self):
        for name in ['gallery','motion']:
            s=(ROOT/'skills/mechanism-figures/assets'/(name+'.html')).read_text()
            self.assertIn('../../../assets/'+name+'.html',s)
            self.assertIn('next.hash=location.hash',s);self.assertIn('next.search=location.search',s)
        self.assertFalse((ROOT/'skills/mechanism-figures/SKILL.md').exists())
    def test_anatomy_credit_and_not_literal_machine_requirements(self):
        s=(ROOT/'docs/ANATOMY_STANDARD.md').read_text()
        self.assertIn('689dcf966e63d92be10a5d593c6e19e10acd4422',s)
        self.assertIn('do not impose a minimum of forty parts',s)
        self.assertIn('code and showcase images were not copied',s)
    def test_eval_cases_are_not_claimed_outcomes(self):
        d=json.loads((ROOT/'evals/evals.json').read_text())
        self.assertEqual(len(d['evals']),8);self.assertIn('not an efficacy study',d['status'])
    def test_capture_never_weakens_browser_security(self):
        s=(ROOT/'scripts/capture.mjs').read_text()
        self.assertNotIn('--no-sandbox',s);self.assertNotIn('--disable-web-security',s)
        self.assertIn('Network.setBlockedURLs',s)
        p=subprocess.run(['node',str(ROOT/'scripts/capture.mjs'),'--help'],capture_output=True,text=True)
        self.assertEqual(p.returncode,0);self.assertIn('4x',p.stdout)


class GeometryTests(unittest.TestCase):
    def test_projection_basis_preserves_3d_norm_with_depth(self):
        p=project([(2,3,4)],azimuth=47,elevation=31)[0]
        self.assertAlmostEqual(sum(x*x for x in p),29)
    def test_vertical_axis_points_up_on_screen(self):
        a,b=project([(0,0,0),(0,0,1)])
        self.assertAlmostEqual(a[0],b[0]);self.assertLess(b[1],a[1])
    def test_fit_uses_one_scale(self):
        result=fit([(0,0),(2,0),(2,1)],400,100,10)
        p=result['points'];self.assertAlmostEqual(math.dist(p[0],p[1])/math.dist(p[1],p[2]),2)
    def test_degenerate_single_point_can_be_centered(self):
        self.assertEqual(fit([(4,4)],100,100)['points'],[(50,50)])
    def test_bad_geometry_rejected(self):
        for f,args in [(project,([(1,float('nan'),0)],)),(fit,([],100,100)),(transform,([(0,1)],(1,2)))]:
            with self.assertRaises(ValueError):f(*args)
    def test_affine_transform_explicit(self):
        self.assertEqual(transform([(1,2)],(2,0,0,2,3,4)),[(5,8)])


class SceneTests(unittest.TestCase):
    def scene(self):return Scene('Fixture','Formal test only; not a scientific result.')
    def add(self,s):
        s.circle('a',(100,100),30,meaning='State a',evidence=['E1'],status='formal')
        s.circle('b',(250,100),30,meaning='State b',evidence=['E1'],status='formal')
        s.anchor('out',(130,100),'a');s.anchor('in',(220,100),'b')
        return s
    def test_identity_evidence_and_anchors_survive_export(self):
        s=self.add(self.scene()).route('update','out','in',meaning='Declared update',evidence=['E1'],status='formal')
        s.label('state-label',(100,150),'State <a>',for_mark='a')
        self.assertIn('State &lt;a&gt;',s.svg());self.assertIn('data-mf-status="formal"',s.svg())
        self.assertEqual(s.marks['update']['points'][0],(130,100))
        self.assertEqual(s.audit()['status'],'geometry_checks_pass')
        self.assertIn('text extent or overlap',s.audit()['not_checked'])
    def test_duplicate_ids_rejected(self):
        s=self.add(self.scene())
        with self.assertRaises(ValueError):s.circle('a',(20,20),10,meaning='x',evidence=['E1'])
    def test_missing_meaning_or_evidence_rejected(self):
        for meaning,evidence in [('', ['E1']),('valid', [])]:
            with self.assertRaises(ValueError):self.scene().circle('a',(20,20),10,meaning=meaning,evidence=evidence)
    def test_undefined_route_endpoint_rejected(self):
        with self.assertRaises(ValueError):self.scene().route('r','a','b',meaning='path',evidence=['E1'])
    def test_anchor_outside_owner_is_not_hidden(self):
        s=self.add(self.scene());s.anchor('bad',(900,900),'a');self.assertTrue(s.audit()['errors'])
        with self.assertRaises(ValueError):s.svg()
    def test_geometry_outside_frame_blocks_export(self):
        s=self.scene().circle('a',(0,0),20,meaning='x',evidence=['E1'])
        with self.assertRaises(ValueError):s.svg()
    def test_physical_type_minimum(self):
        s=self.add(self.scene())
        with self.assertRaises(ValueError):s.label('bad',(100,100),'Too small',for_mark='a',font_pt=5)
    def test_no_active_color_injection(self):
        with self.assertRaises(ValueError):self.scene().circle('a',(20,20),10,meaning='x',evidence=['E1'],fill='url(https://bad.invalid)')
    def test_zero_route_segment_rejected(self):
        s=self.add(self.scene())
        with self.assertRaises(ValueError):s.route('r','out','in',via=[(130,100)],meaning='bad',evidence=['E1'])
    def test_saving_creates_editable_svg_and_scene_record(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'test.svg';s=self.add(self.scene());m=s.save(p)
            self.assertTrue(p.exists());self.assertTrue(p.with_suffix('.scene.json').exists())
            self.assertEqual(len(m['marks']),2)
            with self.assertRaises(FileExistsError):s.save(p)
    def test_degenerate_polygon_rejected(self):
        with self.assertRaises(ValueError):self.scene().polygon('bad',[(1,1),(2,2),(3,3)],meaning='degenerate',evidence=['E1'])


if __name__=='__main__':unittest.main()
