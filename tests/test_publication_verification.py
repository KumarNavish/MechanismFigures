"""Release verifier fixtures test bytes and boundaries, not visual quality."""
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('publication_verifier', ROOT / '.github/scripts/verify_publication.py')
verify = importlib.util.module_from_spec(spec); spec.loader.exec_module(verify)


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.root = Path(self.temp.name)
        self.payload = {'SKILL.md': verify.digest(b'fixture'), 'assets/example.png': verify.digest(b'fixture-pixels')}
    def tearDown(self): self.temp.cleanup()
    def archive(self, kind='skill', extra=False, corrupt=False):
        top = 'mechanism-figures/' if kind == 'skill' else 'mechanism-figures-plugin/'
        prefix = top if kind == 'skill' else top + 'skills/mechanism-figures/'
        data = {prefix + 'SKILL.md': b'fixture', prefix + 'assets/example.png': b'fixture-pixels'}
        if kind == 'plugin': data[top + 'plugin.json'] = b'{}'
        manifest = {'version': '0.5.0', 'kind': kind, 'files': {n: verify.digest(b) for n,b in data.items()}}
        if corrupt: data[prefix + 'SKILL.md'] = b'changed'
        path = self.root / (kind + '.zip')
        with zipfile.ZipFile(path, 'w') as z:
            for n,b in data.items(): z.writestr(n,b)
            z.writestr(top + 'PACKAGE.json', json.dumps(manifest))
            if extra: z.writestr(top + 'unlisted', b'data')
        return path
    def test_standalone_archive_matches_exact_source_payload(self):
        self.assertTrue(verify.inspect_archive(self.archive(), '0.5.0', 'skill', self.payload)['verified'])
    def test_plugin_contains_the_same_exact_skill(self):
        self.assertTrue(verify.inspect_archive(self.archive('plugin'), '0.5.0', 'plugin', self.payload)['verified'])
    def test_corruption_is_not_accepted(self):
        with self.assertRaises(ValueError): verify.inspect_archive(self.archive(corrupt=True), '0.5.0', 'skill', self.payload)
    def test_unmanifested_file_is_not_accepted(self):
        with self.assertRaises(ValueError): verify.inspect_archive(self.archive(extra=True), '0.5.0', 'skill', self.payload)
    def test_self_consistent_but_wrong_payload_fails(self):
        with self.assertRaises(ValueError): verify.inspect_archive(self.archive(), '0.5.0', 'skill', {'SKILL.md': '0'*64})
    def test_wrong_version_fails(self):
        with self.assertRaises(ValueError): verify.inspect_archive(self.archive(), '0.5.1', 'skill', self.payload)
    def test_traversal_and_ambiguous_paths_fail(self):
        for n in ['../x','/x','a/../x','a\\x','a//b','a/./b','']:
            with self.subTest(n=n), self.assertRaises(ValueError): verify.safe_member(n)
    def test_release_target_is_bound_to_tag(self):
        r={'draft':False,'prerelease':False,'tag_name':'v0.5.0','target_commitish':'a'*40,'assets':[]}
        with self.assertRaises(ValueError): verify.verify_downloads(self.root,r,'0.5.0','b'*40,self.payload)
    def test_draft_release_cannot_pass(self):
        with self.assertRaises(ValueError): verify.verify_downloads(self.root,{'draft':True},'0.5.0','a'*40,self.payload)
    def test_gallery_parser_ignores_editorial_sections(self):
        parser=verify.Gallery();parser.feed('<section id="motion"></section><article id="one"></article><article id="two"></article>')
        self.assertEqual(parser.references,['one','two'])


if __name__ == '__main__': unittest.main()
