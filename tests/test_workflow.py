"""Adversarial tooling tests. Synthetic reviews here are fixtures, not quality evidence."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/mechanism-figures'
sys.path.insert(0, str(SKILL / 'scripts'))
from _contract import ValidationError, digest, load_json, preflight, snapshot, svg_checks, validate_contract
from _review import blank_review, evaluate_review, gate, rubric
spec = importlib.util.spec_from_file_location('installer', ROOT / 'tools/install.py')
installer = importlib.util.module_from_spec(spec); spec.loader.exec_module(installer)


def png(width=1080, height=630):
    def chunk(name, data):
        return struct.pack('>I', len(data)) + name + data + struct.pack('>I', zlib.crc32(name + data) & 0xffffffff)
    return b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', width, height, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress((b'\x00' + b'\xff\xff\xff' * width) * height)) + chunk(b'IEND', b'')


def valid_contract():
    c = load_json(SKILL / 'assets/templates/figure.json')
    c.update(id='synthetic-fixture', creator_id='fixture-creator')
    c['inputs'].update(project_context='Tooling fixture; not scientific results.', mechanism='Project a vector onto a halfspace.', evidence=[{'id':'E1','kind':'formal','source':'render.py','local_path':'data.json','supports':'Stated projection formula.','does_not_support':'No empirical speed claim.'}])
    c['inputs']['output_constraints']['audience'] = 'Numerical methods readers'
    c['analysis'].update(insight='The normal component is removed; the tangent is preserved.', entities=[{'id':'v','meaning':'Input vector','units':'dimensionless'}], update_rule='Projection onto x >= 0 is (max(x,0), y).', assumptions=['Euclidean metric.'], claim_boundary='Two-dimensional halfspace only.', falsifier='A tangential coordinate change would contradict this projection.', comparison={'baseline':'Unconstrained vector','held_fixed':['Input and coordinates'],'intervention':'Enforce halfspace','budget':'Analytic operation, no speed comparison.'})
    c['design'].update(candidates=[{'id':'A','construction':'Draw vectors and feasible boundary.','visible_gain':'Shows the removed component.','distortion_risk':'Unequal axes would distort perpendicularity.','evidence_needed':'Exact coordinates.'},{'id':'B','construction':'Align symbolic coordinate transformations.','visible_gain':'Shows unchanged y.','distortion_risk':'Hides Euclidean distance.','evidence_needed':'Exact formula.'}], selected='A', encoding=[{'scientific':'Input vector','visual':'Arrow from origin to v','units':'dimensionless','status':'formal','evidence_ids':['E1']}], reference_readings=[{'id':rid,'image_observed':True,'asset_seen':next(x for x in load_json(SKILL/'assets/calibration.json')['references'] if x['id']==rid)['assets'][0]['path'],'insight':'Fixture declaration only; no real review.','do_not_copy':'Do not transfer domain-specific values.','asset_sha256':next(x for x in load_json(SKILL/'assets/calibration.json')['references'] if x['id']==rid)['assets'][0]['sha256'],'composition_observation':'SYNTHETIC TEST ATTESTATION: fixed geometry.','encoding_observation':'SYNTHETIC TEST ATTESTATION: traceable operator.','style_observation':'SYNTHETIC TEST ATTESTATION: local annotations.','planned_application':'SYNTHETIC TEST ATTESTATION: map the input and operator.'} for rid in ['alphafold','gaussian']], reading_path=['Find the input.','Follow the orthogonal displacement.','Compare preserved tangent.'], prediction_probe={'question':'Which component is preserved?','expected':'The tangential component.'}, counterfactual_probe={'question':'What happens for feasible input?','expected':'It remains unchanged.'})
    c['reproduction'].update(command='python3 render.py', environment='Python standard library fixture')
    return c


def fixture(folder):
    c = valid_contract()
    (folder/'figure.json').write_text(json.dumps(c, indent=2))
    (folder/'figure.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="180mm" height="105mm" viewBox="0 0 1080 630"><title>Projection fixture</title><desc>Synthetic file for tool tests only.</desc><text x="30" y="40" font-size="18">Fixture</text></svg>')
    (folder/'figure.png').write_bytes(png())
    (folder/'caption.md').write_text('Synthetic fixture, not quality evidence.')
    (folder/'render.py').write_text('# Synthetic fixture source, not invoked by the gate.\n')
    (folder/'data.json').write_text('{"vector": [-1, 2]}\n')
    return folder/'figure.json'


def passing_fixture_review(path):
    r = blank_review(path)
    r['observations'].update(viewed_files=['figure.svg','figure.png'], final_size={'width_mm':180,'height_mm':105,'notes':'SYNTHETIC TEST ATTESTATION.'}, captionless={'response':'Tangential component.','prediction':'Feasible input remains fixed.','matches_contract':True,'justification':'Synthetic agreement fixture.','timing':'not_measured'}, grayscale={'inspected':True,'notes':'SYNTHETIC TEST ATTESTATION.'}, reference_comparison=[{'id':rid,'observation':'SYNTHETIC TEST ATTESTATION.','composition_match':'SYNTHETIC TEST ATTESTATION.','encoding_match':'SYNTHETIC TEST ATTESTATION.','style_match':'SYNTHETIC TEST ATTESTATION.','remaining_gap':'SYNTHETIC TEST ATTESTATION.'} for rid in ['alphafold','gaussian']])
    for item in r['gates'].values(): item.update(status='pass',evidence='SYNTHETIC TEST ATTESTATION.',files=['figure.svg'])
    for item in r['scores'].values(): item.update(score=5,evidence='SYNTHETIC TEST ATTESTATION.',residual_issue='This is a test, not independently rated science.')
    r.update(adverse_observation='Entire review is a synthetic fixture.',next_action='Use only to exercise gate logic.')
    return r


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(); self.root = Path(self.tmp.name); self.path = fixture(self.root)
    def tearDown(self): self.tmp.cleanup()
    def write_contract(self, c): self.path.write_text(json.dumps(c))
    def write_review(self, r, name='review.json'):
        p=self.root/name;p.write_text(json.dumps(r));return p
    def test_contract_valid(self): self.assertEqual(validate_contract(load_json(self.path)), [])
    def test_blank_template_cannot_pass(self): self.assertTrue(validate_contract(load_json(SKILL/'assets/templates/figure.json')))
    def test_inputs_stage_does_not_require_design(self):
        c=valid_contract();c['design']={};self.assertEqual(validate_contract(c,'inputs'),[])
    def test_nonfinite_json_rejected(self):
        p=self.root/'bad.json';p.write_text('{"x":NaN}');self.assertRaises(ValidationError,load_json,p)
    def test_duplicate_json_key_rejected(self):
        p=self.root/'bad.json';p.write_text('{"x":1,"x":2}');self.assertRaises(ValidationError,load_json,p)
    def test_missing_units(self):
        c=valid_contract();c['analysis']['entities'][0]['units']='';self.assertTrue(validate_contract(c))
    def test_duplicate_evidence_id(self):
        c=valid_contract();c['inputs']['evidence']*=2;self.assertTrue(validate_contract(c))
    def test_unknown_evidence_reference(self):
        c=valid_contract();c['design']['encoding'][0]['evidence_ids']=['UNSEEN'];self.assertTrue(validate_contract(c))
    def test_blocking_unknown(self):
        c=valid_contract();c['analysis']['unknowns']=[{'id':'u','impact':'blocking','resolved':False}];self.assertTrue(validate_contract(c))
    def test_no_actual_image_inspection(self):
        c=valid_contract()
        for r in c['design']['reference_readings']:r.update(image_observed=False,access_note='No viewer')
        self.assertTrue(validate_contract(c))
    def test_duplicate_constructions(self):
        c=valid_contract();c['design']['candidates'][1]['construction']=c['design']['candidates'][0]['construction'];self.assertTrue(validate_contract(c))
    def test_missing_frozen_prediction(self):
        c=valid_contract();c['design']['counterfactual_probe']['expected']='';self.assertTrue(validate_contract(c))
    def test_safe_fixture_preflight(self): self.assertEqual(preflight(self.path)['errors'],[])
    def test_path_escape_rejected(self):
        c=valid_contract();c['outputs']['source']='../outside.py';self.write_contract(c);self.assertTrue(preflight(self.path)['errors'])
    def test_symlink_rejected(self):
        (self.root/'render.py').unlink();(self.root/'render.py').symlink_to(self.root/'data.json');self.assertTrue(preflight(self.path)['errors'])
    def test_missing_requested_pdf(self):
        c=valid_contract();c['inputs']['output_constraints']['formats'].append('pdf');self.write_contract(c);self.assertTrue(preflight(self.path)['errors'])
    def test_svg_executable_rejected(self):
        p=self.root/'figure.svg';p.write_text(p.read_text().replace('</svg>','<script>alert(1)</script></svg>'));self.assertTrue(preflight(self.path)['errors'])
    def test_svg_external_image_rejected(self):
        p=self.root/'figure.svg';p.write_text(p.read_text().replace('</svg>','<image href="https://example.org/a.png"/></svg>'));self.assertTrue(preflight(self.path)['errors'])
    def test_tiny_type_rejected(self):
        p=self.root/'figure.svg';p.write_text(p.read_text().replace('font-size="18"','font-size="5"'));self.assertTrue(preflight(self.path)['errors'])
    def test_mismatched_physical_size(self):
        p=self.root/'figure.svg';p.write_text(p.read_text().replace('180mm','90mm'));self.assertTrue(preflight(self.path)['errors'])
    def test_fake_png_rejected(self):
        (self.root/'figure.png').write_text('not an image');self.assertTrue(preflight(self.path)['errors'])
    def test_blank_review_does_not_pass(self): self.assertFalse(evaluate_review(self.path,blank_review(self.path))['passed'])
    def test_synthetic_review_policy_path(self): self.assertTrue(evaluate_review(self.path,passing_fixture_review(self.path))['passed'])
    def test_bools_are_not_scores(self):
        r=passing_fixture_review(self.path);r['scores']['visual_intuition']['score']=True;self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_out_of_range_score(self):
        r=passing_fixture_review(self.path);r['scores']['visual_intuition']['score']=6;self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_high_average_does_not_hide_bad_dimension(self):
        r=passing_fixture_review(self.path);r['scores']['annotation_quality']['score']=3;self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_fidelity_must_be_five(self):
        r=passing_fixture_review(self.path);r['scores']['scientific_fidelity']['score']=4;self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_weighted_threshold(self):
        r=passing_fixture_review(self.path)
        for k,v in r['scores'].items():v['score']=5 if k=='scientific_fidelity' else 4
        self.assertEqual(evaluate_review(self.path,r)['weighted_score'],84);self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_unknown_gate_blocks(self):
        r=passing_fixture_review(self.path);r['gates']['no_clipping']['status']='unknown';self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_scores_without_evidence_block(self):
        r=passing_fixture_review(self.path);r['scores']['aesthetic_refinement']['evidence']='';self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_failed_captionless_prediction_blocks(self):
        r=passing_fixture_review(self.path);r['observations']['captionless']['matches_contract']=False;self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_stale_vector_blocks(self):
        r=passing_fixture_review(self.path);p=self.root/'figure.svg';p.write_text(p.read_text()+'\n');self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_stale_source_blocks(self):
        r=passing_fixture_review(self.path);(self.root/'render.py').write_text('# changed');self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_stale_evidence_blocks(self):
        r=passing_fixture_review(self.path);(self.root/'data.json').write_text('{}');self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_stale_claim_blocks(self):
        r=passing_fixture_review(self.path);c=load_json(self.path);c['analysis']['insight']='Changed assertion';self.write_contract(c);self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_self_review_is_not_independent(self):
        p=self.write_review(passing_fixture_review(self.path));self.assertEqual(gate(self.path,[p])['status'],'self_review_pass');self.assertEqual(gate(self.path,[p],True)['status'],'needs_independent_review')
    def test_same_author_cannot_be_independent(self):
        r=passing_fixture_review(self.path);r['reviewer']['mode']='independent';self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_independent_attestation_needs_response_file(self):
        r=passing_fixture_review(self.path);r['reviewer']={'id':'fixture-reader','mode':'independent'};self.assertFalse(evaluate_review(self.path,r)['passed'])
    def test_independent_gate_fixture_requires_both_reviews(self):
        a=self.write_review(passing_fixture_review(self.path),'self.json');r=passing_fixture_review(self.path);r['reviewer']={'id':'fixture-reader','mode':'independent'}
        response=self.root/'reader.txt';response.write_text('SYNTHETIC TEST RESPONSE. Not a reader study.')
        r['observations']['response_record']={'path':'reader.txt','sha256':digest(response)};b=self.write_review(r,'independent.json')
        self.assertEqual(gate(self.path,[a,b],True)['status'],'independent_review_pass');self.assertEqual(gate(self.path,[b],True)['status'],'needs_revision')
    def test_init_refuses_existing_directory(self):
        p=subprocess.run([sys.executable,str(SKILL/'scripts/mf.py'),'init',str(self.root)],capture_output=True,text=True);self.assertEqual(p.returncode,2)
    def test_review_init_does_not_overwrite(self):
        out=self.root/'review.json';out.write_text('preserve me')
        p=subprocess.run([sys.executable,str(SKILL/'scripts/mf.py'),'review-init',str(self.path),'--out',str(out)],capture_output=True,text=True)
        self.assertEqual(p.returncode,2);self.assertEqual(out.read_text(),'preserve me')
    def test_rubric_weights(self): self.assertEqual(sum(x['weight'] for x in rubric()['dimensions']),100)


class InstallTests(unittest.TestCase):
    def setUp(self): self.tmp=tempfile.TemporaryDirectory();self.dest=Path(self.tmp.name)/'skills'
    def tearDown(self): self.tmp.cleanup()
    def test_clean_idempotent_install_and_check(self):
        self.assertEqual(installer.install(self.dest)['status'],'installed')
        self.assertEqual(installer.install(self.dest)['status'],'already_installed')
        self.assertEqual(installer.install(self.dest,True)['status'],'verified')
        result=subprocess.run([sys.executable,str(self.dest/'mechanism-figures/scripts/mf.py'),'references','--bundled'],capture_output=True,text=True)
        self.assertEqual(result.returncode,0);self.assertIn('alphafold',result.stdout)
    def test_refuse_unknown_destination(self):
        (self.dest/'mechanism-figures').mkdir(parents=True);self.assertRaises(ValueError,installer.install,self.dest)
    def test_preserve_modified_installation(self):
        installer.install(self.dest);p=self.dest/'mechanism-figures/SKILL.md';p.write_text('my edits');self.assertRaises(ValueError,installer.install,self.dest);self.assertEqual(p.read_text(),'my edits')
    def test_check_never_installs(self):
        self.assertRaises(ValueError,installer.install,self.dest,True);self.assertFalse(self.dest.exists())
    def test_refuse_destination_symlink(self):
        self.dest.mkdir();(self.dest/'mechanism-figures').symlink_to(SKILL,target_is_directory=True);self.assertRaises(ValueError,installer.install,self.dest)


if __name__ == '__main__': unittest.main()
