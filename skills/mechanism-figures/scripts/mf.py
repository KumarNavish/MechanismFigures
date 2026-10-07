#!/usr/bin/env python3
"""MechanismFigures: small offline helpers, never an autonomous model runner."""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys

from _contract import SKILL, ValidationError, load_json, preflight, snapshot, validate_contract
from _review import blank_review, gate


def emit(obj):
    print(json.dumps(obj, indent=2, ensure_ascii=False, allow_nan=False))


def exclusive_json(path: Path, obj):
    with path.open('x', encoding='utf-8') as out:
        json.dump(obj, out, indent=2, ensure_ascii=False, allow_nan=False)
        out.write('\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('init', help='Create one isolated work folder; never overwrite')
    p.add_argument('directory', type=Path)
    p = sub.add_parser('validate', help='Validate an input or planned figure contract')
    p.add_argument('contract', type=Path); p.add_argument('--stage', choices=['inputs', 'plan'], default='plan')
    p = sub.add_parser('preflight', help='Check artifacts, formats, paths, and SVG metadata')
    p.add_argument('contract', type=Path)
    p = sub.add_parser('review-init', help='Bind a blank review to the current file hashes')
    p.add_argument('contract', type=Path); p.add_argument('--out', type=Path, required=True)
    p = sub.add_parser('gate', help='Evaluate recorded human/agent review against policy')
    p.add_argument('contract', type=Path); p.add_argument('reviews', type=Path, nargs='+')
    p.add_argument('--require-independent', action='store_true')
    p = sub.add_parser('references', help='List concise calibration routes')
    p.add_argument('--group', choices=['structure', 'transformation', 'dynamics', 'evidence', 'invariance', 'contrast'])
    p.add_argument('--bundled', action='store_true')
    p = sub.add_parser('reference', help='Read one construction recipe, not the full atlas')
    p.add_argument('id'); p.add_argument('--json', action='store_true')
    p = sub.add_parser('revision', help='Append an explicit repair record, preserving history')
    p.add_argument('contract', type=Path); p.add_argument('--issue', required=True)
    p.add_argument('--change', required=True); p.add_argument('--observation', required=True)
    p.add_argument('--status', choices=['needs_revision', 'needs_evidence', 'needs_visual_review', 'needs_independent_review', 'self_review_pass', 'independent_review_pass'], default='needs_revision')
    args = parser.parse_args(argv)
    try:
        if args.command == 'init':
            dest = args.directory.expanduser().absolute()
            if dest.exists(): raise ValidationError('Refusing to replace an existing directory: ' + str(dest))
            template = load_json(SKILL / 'assets/templates/figure.json')
            template['id'] = dest.name
            dest.mkdir(parents=True, exist_ok=False)
            exclusive_json(dest / 'figure.json', template)
            (dest / 'revisions.jsonl').touch(exist_ok=False)
            emit({'status': 'initialized', 'contract': str(dest / 'figure.json'), 'next': 'Fill the four inputs, then follow SKILL.md. Empty templates cannot pass validation.'})
        elif args.command == 'validate':
            errors = validate_contract(load_json(args.contract), args.stage)
            emit({'status': 'contract_valid' if not errors else 'needs_contract', 'errors': errors})
            return 0 if not errors else 2
        elif args.command == 'preflight':
            result = preflight(args.contract); emit(result)
            return 0 if not result['errors'] else 2
        elif args.command == 'review-init':
            exclusive_json(args.out, blank_review(args.contract))
            emit({'status': 'review_initialized', 'review': str(args.out), 'next': 'Inspect actual artifacts; no score or gate has been filled for you.'})
        elif args.command == 'gate':
            result = gate(args.contract, args.reviews, args.require_independent); emit(result)
            return 0 if result['accepted'] else 2
        elif args.command in {'references', 'reference'}:
            refs = load_json(SKILL / 'assets/calibration.json')['references']
            if args.command == 'references':
                emit([{'id': r['id'], 'move': r['transfer']['move'], 'group': r['transfer']['group'],
                       'bundled': bool(r['assets']), 'case': str(SKILL / 'references/cases' / (r['id'] + '.md'))}
                      for r in refs if (not args.group or r['transfer']['group'] == args.group) and (not args.bundled or r['assets'])])
            else:
                result = next((r for r in refs if r['id'] == args.id), None)
                if result is None: raise ValidationError('Unknown reference ID: ' + args.id)
                if args.json: emit(result)
                else: print((SKILL / 'references/cases' / (args.id + '.md')).read_text())
        elif args.command == 'revision':
            record = {'timestamp_utc': datetime.now(timezone.utc).isoformat(), 'snapshot': snapshot(args.contract),
                      'issue': args.issue, 'change': args.change, 'observation': args.observation,
                      'declared_status': args.status, 'costs': {'tokens': None, 'wall_seconds': None, 'compute_seconds': None},
                      'notice': 'Append-only author attestation; status is not a replacement for a fresh gate result.'}
            log = args.contract.resolve().parent / 'revisions.jsonl'
            if log.is_symlink(): raise ValidationError('Revision log cannot be a symlink')
            with log.open('a', encoding='utf-8') as out: out.write(json.dumps(record, ensure_ascii=False) + '\n')
            emit({'status': 'revision_recorded', 'log': str(log)})
        return 0
    except (ValidationError, OSError, ValueError, TypeError, KeyError) as exc:
        emit({'status': 'invalid_input', 'error': str(exc)})
        return 2


if __name__ == '__main__':
    sys.exit(main())
