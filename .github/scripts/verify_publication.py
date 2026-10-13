#!/usr/bin/env python3
"""Read-only validation of already-published packages and Pages, never an installer."""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import importlib.util
import json
from pathlib import Path, PurePosixPath
import re
import stat
import urllib.request
import zipfile

BASE = 'https://kumarnavish.github.io/MechanismFigures/'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_member(name):
    p = PurePosixPath(name)
    if not name or p.is_absolute() or '..' in p.parts or '\\' in name or str(p) != name:
        raise ValueError('Unsafe archive name: ' + name)
    return p


def inspect_archive(path, version, kind, payload):
    """Compare every archived payload byte with the reviewed source. No extraction."""
    top = 'mechanism-figures/' if kind == 'skill' else 'mechanism-figures-plugin/'
    prefix = top if kind == 'skill' else top + 'skills/mechanism-figures/'
    with zipfile.ZipFile(path) as archive:
        infos = archive.infolist()
        names = [i.filename for i in infos]
        if len(names) > 2000 or len(set(names)) != len(names):
            raise ValueError('Duplicate or excessive archive members')
        if sum(i.file_size for i in infos) > 150_000_000:
            raise ValueError('Archive uncompressed size exceeds inspection bound')
        for i in infos:
            safe_member(i.filename)
            if not i.filename.startswith(top) or i.is_dir() or stat.S_ISLNK(i.external_attr >> 16):
                raise ValueError('Unexpected archive member type/root: ' + i.filename)
        manifest_name = top + 'PACKAGE.json'
        manifest = json.loads(archive.read(manifest_name))
        if manifest['version'] != version or manifest['kind'] != kind:
            raise ValueError('Archive identity mismatch')
        if set(names) != set(manifest['files']) | {manifest_name}:
            raise ValueError('Unmanifested or missing archive members')
        for name, sha in manifest['files'].items():
            if digest(archive.read(name)) != sha:
                raise ValueError('Manifest checksum mismatch: ' + name)
        archived = {name[len(prefix):]: sha for name, sha in manifest['files'].items() if name.startswith(prefix)}
        if archived != payload:
            raise ValueError('Published skill payload differs from reviewed source')
        if sum(n.endswith('/SKILL.md') for n in names) != 1:
            raise ValueError('Expected exactly one discoverable skill')
    return {'kind': kind, 'files': len(names), 'payload_files': len(payload), 'sha256': digest(Path(path).read_bytes()), 'verified': True}


def verify_downloads(directory, release, version, commit, payload):
    if release.get('draft') or release.get('prerelease') or release.get('tag_name') != 'v' + version:
        raise ValueError('Not the requested final release')
    if release.get('target_commitish') != commit:
        raise ValueError('Release target differs from resolved tag commit')
    assets = {a['name']: a for a in release['assets']}
    result = []
    for kind, infix in [('skill', ''), ('plugin', 'plugin-')]:
        name = 'mechanism-figures-' + infix + 'v' + version + '.zip'
        sidecar = name + '.sha256'
        for filename in [name, sidecar]:
            entry = assets[filename]
            data = (directory / filename).read_bytes()
            if entry.get('state') != 'uploaded' or entry.get('size') != len(data):
                raise ValueError('Incomplete release asset: ' + filename)
            if entry.get('digest') != 'sha256:' + digest(data):
                raise ValueError('Release API digest mismatch: ' + filename)
        parts = (directory / sidecar).read_text().strip().split()
        if parts != [digest((directory / name).read_bytes()), name]:
            raise ValueError('Checksum sidecar mismatch: ' + name)
        result.append(inspect_archive(directory / name, version, kind, payload))
    return result


class Gallery(HTMLParser):
    def __init__(self):
        super().__init__(); self.references = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'article': self.references.append(a.get('id'))


def load_public(root, relative):
    safe_member(relative)
    local = root / relative
    expected = digest(local.read_bytes())
    url = BASE + relative + '?verified=' + expected[:16]
    request = urllib.request.Request(url, headers={'Cache-Control': 'no-cache', 'User-Agent': 'MechanismFigures-publication-verifier'})
    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status != 200 or not response.geturl().startswith(BASE):
            raise ValueError('Unexpected public response: ' + relative)
        data = response.read(50_000_001)
    if len(data) > 50_000_000 or digest(data) != expected:
        raise ValueError('Deployed bytes differ from reviewed source: ' + relative)
    return {'path': relative, 'bytes': len(data), 'sha256': expected, 'verified': True}


def verify_pages(root):
    registry = json.loads((root / 'assets/calibration.json').read_text())
    refs = registry['references']
    image_paths = [a['path'] for r in refs for a in r['assets']]
    for r in refs:
        for a in r['assets']:
            if digest((root / a['path']).read_bytes()) != a['sha256']:
                raise ValueError('Local calibration integrity mismatch: ' + r['id'])
    parser = Gallery(); parser.feed((root / 'assets/gallery.html').read_text())
    if parser.references != [r['id'] for r in refs]:
        raise ValueError('Gallery reference membership/order mismatch')
    paths = ['index.html', 'assets/gallery.html', 'assets/motion.html', 'assets/calibration.json', 'assets/approved-canon.json'] + image_paths
    for name in ['gallery', 'motion']:
        path = 'skills/mechanism-figures/assets/' + name + '.html'
        text = (root / path).read_text()
        if '../../../assets/' + name + '.html' not in text or 'next.search=location.search' not in text or 'next.hash=location.hash' not in text:
            raise ValueError('Legacy route lost target/query/fragment compatibility')
        paths.append(path)
    with ThreadPoolExecutor(max_workers=4) as pool:
        files = list(pool.map(lambda p: load_public(root, p), paths))
    return {'reference_count': len(refs), 'image_count': len(image_paths), 'files': files,
            'note': 'Public HTTP byte verification. Separate CI renders exercise browser behavior; this does not attest to human comprehension.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--packages', type=Path, required=True)
    parser.add_argument('--metadata', type=Path, required=True)
    parser.add_argument('--release-commit', required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    report = {'verified': False, 'checked_at': datetime.now(timezone.utc).isoformat(),
              'scope': 'Public repository/release/Pages only. No Mac update, host activation, model execution or scientific-quality certification.'}
    try:
        version = (root / 'VERSION').read_text().strip()
        if not re.fullmatch(r'\d+\.\d+\.\d+', version) or not re.fullmatch(r'[0-9a-f]{40}', args.release_commit):
            raise ValueError('Invalid version or commit')
        spec = importlib.util.spec_from_file_location('payload_inventory', root / 'tools/install.py')
        installer = importlib.util.module_from_spec(spec); spec.loader.exec_module(installer)
        payload = installer.inventory(root)
        release = json.loads(args.metadata.read_text())
        report.update(version=version, release_commit=args.release_commit, release_url=release.get('html_url'))
        report['archives'] = verify_downloads(args.packages, release, version, args.release_commit, payload)
        report['pages'] = verify_pages(root)
        report['verified'] = True
    except Exception as exc:
        report['error'] = type(exc).__name__ + ': ' + str(exc)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: v for k, v in report.items() if k not in {'pages'}}))
    return 0 if report['verified'] else 2


if __name__ == '__main__':
    raise SystemExit(main())
