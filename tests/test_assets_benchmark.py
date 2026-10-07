import base64
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from test_workflow import ROOT, SKILL, fixture, png, valid_contract, passing_fixture_review
from _contract import ValidationError, preflight, validate_contract, snapshot

spec=importlib.util.spec_from_file_location('benchmark_report',ROOT/'tools/benchmark_report.py')
reporter=importlib.util.module_from_spec(spec);spec.loader.exec_module(reporter)
spec2=importlib.util.spec_from_file_location('analytical_examples',ROOT/'examples/render_examples.py')
examples=importlib.util.module_from_spec(spec2);spec2.loader.exec_module(examples)


class AssetTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name);self.path=fixture(self.root)
    def tearDown(self):self.tmp.cleanup()
    def insert(self,markup):
        p=self.root/'figure.svg';p.write_text(p.read_text().replace('</svg>',markup+'</svg>'))
    def test_real_embedded_raster_is_allowed(self):
        self.insert('<image x="0" y="0" width="10" height="10" href="data:image/png;base64,'+base64.b64encode(png(2,2)).decode()+'"/>')
        self.assertEqual(preflight(self.path)['errors'],[])
    def test_active_embedded_svg_is_rejected(self):
        self.insert('<image href="data:image/svg+xml;base64,PHN2Zy8+"/>');self.assertTrue(preflight(self.path)['errors'])
    def test_wrong_embedded_mime_signature_is_rejected(self):
        self.insert('<image href="data:image/png;base64,YWJj"/>');self.assertTrue(preflight(self.path)['errors'])
    def test_quoted_local_fragment_is_allowed(self):
        self.insert('<defs><linearGradient id="g"><stop offset="0" stop-color="white"/></linearGradient></defs><rect width="10" height="10" style="fill:url(\'#g\')"/>')
        self.assertEqual(preflight(self.path)['errors'],[])
    def test_external_css_url_is_rejected(self):
        self.insert('<style>.x{fill:url(https://example.org/a)}</style>');self.assertTrue(preflight(self.path)['errors'])
    def test_reference_file_must_belong_to_selected_reference(self):
        c=valid_contract();c['design']['reference_readings'][0]['asset_seen']='assets/calibration/nonexistent.png';self.assertTrue(validate_contract(c))
    def test_reference_url_cannot_be_arbitrary(self):
        c=valid_contract();c['design']['reference_readings'][0]['asset_seen']='https://example.org/unrelated.png';self.assertTrue(validate_contract(c))
    def test_snapshot_binds_rubric(self):self.assertIn('rubric_sha256',snapshot(self.path))
    def test_analytical_examples_satisfy_equations(self):self.assertTrue(all(examples.check_math().values()))


class BenchmarkTests(unittest.TestCase):
    def setUp(self):self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def test_no_runs_is_not_success_or_failure(self):self.assertEqual(reporter.report(self.root/'absent.jsonl')['status'],'not_run')
    def rows(self):
        rows=[]
        for condition in ['baseline','skill']:
            p=self.root/condition;p.mkdir();contract=fixture(p)
            (p/'review.json').write_text(json.dumps(passing_fixture_review(contract)))
            rows.append({'task':'fixture','agent':'fixture-agent','seed':1,'condition':condition,'input_packet_sha256':'0'*64,'budget':{'tokens':100},'contract':condition+'/figure.json','reviews':[condition+'/review.json'],'costs':{'tokens':None,'wall_seconds':None,'tool_calls':None,'compute_seconds':None}})
        return rows
    def save(self,rows):
        p=self.root/'runs.jsonl';p.write_text('\n'.join(json.dumps(r) for r in rows));return p
    def test_self_reviews_never_become_independent_outcomes(self):
        r=reporter.report(self.save(self.rows()));self.assertEqual(r['matched_pairs'],1);self.assertEqual(r['conditions']['skill']['passed'],0);self.assertEqual(r['conditions']['skill']['missing_cost_counts']['tokens'],1)
    def test_unmatched_budgets_rejected(self):
        rows=self.rows();rows[1]['budget']={'tokens':200};self.assertRaises(ValidationError,reporter.report,self.save(rows))
    def test_duplicate_runs_rejected(self):
        rows=self.rows();rows.append(rows[0]);self.assertRaises(ValidationError,reporter.report,self.save(rows))
    def test_negative_costs_rejected(self):
        rows=self.rows();rows[0]['costs']['tokens']=-1;self.assertRaises(ValidationError,reporter.report,self.save(rows))


if __name__=='__main__':unittest.main()
