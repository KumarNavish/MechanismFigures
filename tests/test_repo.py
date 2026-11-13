"""Repository checks: registry, generated files, links, install payload and one real render."""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
CHROME = [p for p in ['/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/google-chrome-stable', '/usr/bin/chromium', '/usr/bin/chromium-browser'] if Path(p).exists()]


class Repo(unittest.TestCase):
    def test_registry_and_generated_files_are_current(self):
        r = subprocess.run([sys.executable, 'tools/build.py', '--check'], cwd=ROOT, capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout)

    def test_atlas_keeps_its_3d_bias_and_its_history(self):
        data = json.loads((ROOT / 'assets/references.json').read_text())
        refs = data['references']
        self.assertGreaterEqual(sum(r['dim'] != 'flat' for r in refs) / len(refs), 0.75)
        self.assertNotEqual(refs[0]['dim'], 'flat')
        self.assertFalse({r['id'] for r in refs} & set(data['retired_ids']))
        for move in data['moves']:
            self.assertTrue(any(move in r['moves'] for r in refs), 'no reference teaches the move ' + move)

    def test_skill_entry_point(self):
        text = (ROOT / 'SKILL.md').read_text()
        self.assertTrue(text.startswith('---\nname: mechanism-figures\n'))
        self.assertLess(len(text.splitlines()), 220)
        description = re.search(r'^description: (.+)$', text, re.M)[1]
        self.assertLessEqual(len(description), 1024)
        self.assertIn((ROOT / 'VERSION').read_text().strip(), text)

    def test_local_links_resolve(self):
        for p in [ROOT / 'SKILL.md', ROOT / 'README.md', ROOT / 'AGENTS.md', *ROOT.glob('references/**/*.md'), *ROOT.glob('docs/*.md')]:
            for target in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', p.read_text()):
                if not target.startswith(('http://', 'https://', 'mailto:')):
                    self.assertTrue((p.parent / target).exists(), f'{p.relative_to(ROOT)} -> {target}')

    def test_no_private_path_or_secret(self):
        for p in ROOT.rglob('*'):
            if p.is_file() and p.suffix in {'.md', '.json', '.py', '.mjs', '.yml', '.html', '.css', '.js'} and p.name != 'test_repo.py' and not {'.git', '.work', '.build', 'vendor'} & set(p.parts):
                self.assertIsNone(re.search(r'/Users/[A-Za-z0-9_]+/|sk-proj-|github_pat_', p.read_text()), str(p))

    def test_reference_lookup(self):
        out = subprocess.run([sys.executable, 'scripts/refs.py', 'cutaway'], cwd=ROOT, capture_output=True, text=True).stdout
        self.assertIn('kent-hopfion', out)
        self.assertTrue(all(Path(l.split('image: ')[1]).is_file() for l in out.splitlines() if 'image: ' in l))

    def test_installed_payload_is_the_working_skill(self):
        from install import install
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(install(Path(tmp))['path'])
            for name in ['SKILL.md', 'scripts/render.mjs', 'scripts/refs.py', 'kit/stage.mjs', 'kit/template.mjs', 'kit/vendor/three.module.min.js', 'assets/references.json', 'references/atlas.md', 'THIRD_PARTY.md']:
                self.assertTrue((dest / name).is_file(), name)
            self.assertFalse((dest / 'tools').exists())
            self.assertFalse((dest / 'tests').exists())

    @unittest.skipUnless(shutil.which('node') and CHROME, 'needs Node and Chrome')
    def test_stage_renders_the_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(['node', 'scripts/render.mjs', 'kit/template.mjs', '--out', tmp, '--scale', '2', '--tiles', '1'], cwd=ROOT, capture_output=True, text=True, timeout=240)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            report = json.loads(r.stdout)
            self.assertEqual(report['warnings'], [])
            self.assertEqual(report['errors'], [])
            for name in ['template-beat1.png', 'template-beat3.png', 'template-beat3.svg', 'template-beat3-gray.png', 'template-story.html']:
                self.assertGreater((Path(tmp) / name).stat().st_size, 2000, name)
            self.assertIn('<text', (Path(tmp) / 'template-beat3.svg').read_text())


if __name__ == '__main__':
    unittest.main()
