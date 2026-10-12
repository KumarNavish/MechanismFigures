#!/usr/bin/env python3
"""Offline, atomic Agent Skills installation. Never overwrite modified or unknown skills."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT
PAYLOAD_DIRS = {'assets','references','scripts','kit','agents','docs','tools','benchmarks','evals'}
PAYLOAD_FILES = {'SKILL.md','README.md','LICENSE','THIRD_PARTY.md','VERSION','AGENTS.md','START_HERE.md','llms.txt','CONTRIBUTING.md','SECURITY.md','CHANGELOG.md','install.py','plugin.json'}
NAME = 'mechanism-figures'
MARKER = '.mechanismfigures-install.json'


def inventory(root):
    result = {}
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if Path(root).resolve() == SOURCE.resolve() and rel.parts[0] not in PAYLOAD_DIRS | PAYLOAD_FILES:
            continue
        if '__pycache__' in rel.parts or path.name in {'.DS_Store', MARKER} or path.suffix == '.pyc': continue
        if path.is_symlink(): raise ValueError('Symlinks are not permitted in the install tree: ' + str(rel))
        if path.is_file(): result[rel.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result



def copy_payload(source, target, expected):
    """Copy only inspected inventory entries, never .git, jobs, or local work files."""
    target.mkdir(parents=True, exist_ok=False)
    for name in expected:
        rel = Path(name)
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError('Invalid payload path: ' + name)
        origin = Path(source) / rel
        if origin.is_symlink() or not origin.is_file():
            raise ValueError('Payload changed since inspection: ' + name)
        dest = target / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origin, dest)
    if inventory(target) != expected:
        raise ValueError('Payload copy differs from inspected inventory')


def install(destination, check_only=False, source=SOURCE):
    source = Path(source).resolve()
    target = Path(destination).expanduser().absolute() / NAME
    if not (source / 'SKILL.md').is_file(): raise ValueError('Missing SKILL.md in source tree')
    expected = inventory(source)
    if target.is_symlink(): raise ValueError('Destination skill is a symlink; refusing to follow it')
    if target.exists():
        marker = target / MARKER
        if not marker.is_file(): raise ValueError('Existing destination is not a managed installation; it is unchanged')
        recorded = json.loads(marker.read_text())
        actual = inventory(target)
        if recorded.get('files') != actual:
            raise ValueError('Installed files were modified; preserve them and install into a new skills root')
        if actual != expected:
            raise ValueError('Different version already installed; use a new skills root to review the update before replacing it')
        return {'status': 'verified' if check_only else 'already_installed', 'path': str(target), 'files': len(actual)}
    if check_only: raise ValueError('Skill is not installed at ' + str(target))
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = Path(tempfile.mkdtemp(prefix='.mechanismfigures-', dir=str(target.parent)))
    try:
        staged = temp / NAME
        copy_payload(source, staged, expected)
        if inventory(staged) != expected: raise ValueError('Copy verification failed; no installation was committed')
        (staged / MARKER).write_text(json.dumps({'schema_version': 1, 'version': '0.5.0', 'files': expected}, indent=2) + '\n')
        if target.exists(): raise ValueError('Destination appeared during installation; no overwrite attempted')
        staged.rename(target)
    finally:
        shutil.rmtree(temp)
    return {'status': 'installed', 'path': str(target), 'files': len(expected),
            'next': 'Reload your agent skill discovery, or explicitly open the installed SKILL.md. No agent was invoked.'}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path.home() / '.agents/skills', help='Skills root; a mechanism-figures child is created')
    parser.add_argument('--check', action='store_true', help='Read-only verification against this checkout')
    args = parser.parse_args(argv)
    try:
        print(json.dumps(install(args.dest, args.check), indent=2))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({'status': 'not_installed', 'error': str(exc)}, indent=2)); return 2


if __name__ == '__main__': sys.exit(main())
