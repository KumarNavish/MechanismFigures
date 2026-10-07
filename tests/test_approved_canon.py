"""The approved real-image canon is the only visual calibration source."""
import copy
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import tempfile
import unittest
from test_workflow import ROOT,SKILL,fixture,valid_contract,passing_fixture_review
from _contract import load_json,validate_contract,snapshot
from _review import evaluate_review


class GalleryHTML(HTMLParser):
    def __init__(self):super().__init__();self.ids=[];self.images=[];self.sections=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if tag=='section':self.sections.append(a.get('id'))
        if tag=='article':self.ids.append(a.get('id'))
        if tag=='img' and 'gallery' in self.sections:self.images.append(a.get('src'))
    def handle_endtag(self,tag):
        if tag=='section' and self.sections:self.sections.pop()


class ApprovedCanonTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.path=fixture(Path(self.tmp.name))
    def tearDown(self):self.tmp.cleanup()
    def test_all_twenty_approved_references_have_real_images(self):
        data=load_json(SKILL/'assets/calibration.json');canon=load_json(SKILL/'assets/approved-canon.json')
        self.assertEqual([r['id'] for r in data['references']],canon['approved_ids'])
        self.assertEqual(len(data['references']),20)
        for r in data['references']:
            self.assertTrue(r['assets']);self.assertTrue(r['display_assets'])
            self.assertTrue(all(a['origin']=='published-reference' for a in r['assets']))
    def test_original_six_anchors_appear_first(self):
        refs=load_json(SKILL/'assets/calibration.json')['references']
        self.assertEqual([r['id'] for r in refs[:6]],['alphafold','cellrank','graphcast','dreamfusion','alphadev','aardvark'])
    def test_all_29_asset_files_have_matching_hashes(self):
        assets=[a for r in load_json(SKILL/'assets/calibration.json')['references'] for a in r['assets']]
        self.assertEqual(len(assets),29)
        self.assertEqual(len({a['path'] for a in assets}),29)
        for a in assets:self.assertEqual(hashlib.sha256((SKILL/a['path']).read_bytes()).hexdigest(),a['sha256'])
    def test_gallery_contains_every_reference_image_without_javascript(self):
        parser=GalleryHTML();parser.feed((SKILL/'assets/gallery.html').read_text())
        self.assertEqual(len(parser.ids),20);self.assertEqual(len(parser.images),21)
        for src in parser.images:
            self.assertFalse(src.startswith(('http:','https:','data:')))
            self.assertTrue((SKILL/'assets'/src).is_file())
    def test_gallery_has_no_text_only_or_generated_substitutes(self):
        s=(SKILL/'assets/gallery.html').read_text()
        self.assertNotIn('class="source-only"',s)
        self.assertNotIn('examples/generated',s)
        self.assertFalse((ROOT/'examples').exists())
    def test_two_observed_reference_images_are_required(self):
        c=valid_contract();c['design']['reference_readings'][1]['image_observed']=False
        self.assertTrue(validate_contract(c))
    def test_missing_reference_image_hash_blocks(self):
        c=valid_contract();del c['design']['reference_readings'][0]['asset_sha256'];self.assertTrue(validate_contract(c))
    def test_incorrect_reference_image_hash_blocks(self):
        c=valid_contract();c['design']['reference_readings'][0]['asset_sha256']='0'*64;self.assertTrue(validate_contract(c))
    def test_self_generated_reference_path_blocks(self):
        c=valid_contract();c['design']['reference_readings'][0]['asset_seen']='my-generated-reference.svg';self.assertTrue(validate_contract(c))
    def test_every_visual_observation_field_is_required(self):
        for field in ['composition_observation','encoding_observation','style_observation','planned_application']:
            c=valid_contract();c['design']['reference_readings'][0][field]='';self.assertTrue(validate_contract(c),field)
    def test_reference_style_comparison_is_required_in_review(self):
        for field in ['composition_match','encoding_match','style_match','remaining_gap']:
            r=passing_fixture_review(self.path);del r['observations']['reference_comparison'][0][field]
            self.assertFalse(evaluate_review(self.path,r)['passed'],field)
    def test_review_snapshot_binds_the_calibration_registry(self):
        self.assertIn('calibration_sha256',snapshot(self.path))
    def test_all_case_files_have_reference_specific_style_lessons(self):
        for r in load_json(SKILL/'assets/calibration.json')['references']:
            case=(SKILL/'references/cases'/(r['id']+'.md')).read_text()
            self.assertIn(r['visual_style']['observed'],case)
            self.assertIn(r['visual_style']['apply'],case)
            self.assertIn('asset_sha256',(SKILL/'references/style-calibration.md').read_text())


if __name__=='__main__':unittest.main()
