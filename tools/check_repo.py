#!/usr/bin/env python3
"""Audit the portable skill, public assets and local links without network access."""
import ast
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/mechanism-figures'
EXCLUDED={'.git','.work','.build','.local-calibration','__pycache__'}


def audit():
    errors=[]
    data=json.loads((SKILL/'assets/calibration.json').read_text())
    refs=data['references'];ids=[r['id'] for r in refs]
    if len(ids)!=len(set(ids)):errors.append('Duplicate calibration IDs')
    canon=json.loads((SKILL/'assets/approved-canon.json').read_text())
    if ids != canon['approved_ids'] or len(ids)!=20:errors.append('Approved twenty-reference canon changed')
    if ids[:6] != canon['core_ids']:errors.append('Current recorded anchors must appear first')
    if (ROOT/'examples').exists():errors.append('Self-generated examples must not be shipped as the visual standard')
    expected_assets=set()
    for r in refs:
        if len(r['transfer']['trace'])!=3 or len(r['transfer']['build'])!=3:errors.append('Missing concrete three-step recipe: '+r['id'])
        if not r['assets'] or not r.get('display_assets'):errors.append('Approved reference has no visible image: '+r['id'])
        if r['rights']['status'] not in {'bundled','reference-excerpt'}:errors.append('Unknown image-rights record: '+r['id'])
        if r['rights']['status']=='bundled' and r['rights']['license']!='CC-BY-4.0':errors.append('Do not invent a verified reusable image license')
        if not r.get('visual_style',{}).get('observed') or not r.get('visual_style',{}).get('apply'):errors.append('Missing reference-specific style lesson')
        if any(p not in {a['path'] for a in r['assets']} for p in r.get('display_assets',[])):errors.append('Displayed image not registered to its reference')
        for a in r['assets']:
            p=SKILL/a['path'];expected_assets.add(p.resolve())
            if not p.is_file() or p.is_symlink():errors.append('Missing/symlink image '+a['path']);continue
            b=p.read_bytes()
            if hashlib.sha256(b).hexdigest()!=a['sha256'] or len(b)!=a['bytes']:errors.append('Asset integrity mismatch: '+a['path'])
            if not a['treatment'] or not r['rights']['basis_url']:errors.append('Missing credit/treatment record')
            if a.get('origin')!='published-reference':errors.append('Only real published reference images are allowed')
        case=SKILL/'references/cases'/(r['id']+'.md')
        if not case.is_file():errors.append('Missing case '+r['id'])
    actual={p.resolve() for p in (SKILL/'assets/calibration').glob('*') if p.is_file()}
    if expected_assets!=actual:errors.append('Untracked or missing calibration image bytes')
    if len(actual)!=29:errors.append('The full approved set contains 29 image assets')
    skill=(SKILL/'SKILL.md').read_text()
    if not skill.startswith('---\n') or len(skill.splitlines())>=500:errors.append('Invalid/oversized skill entry point')
    match=re.search(r'^name: (.+)$',skill,re.M)
    if not match or match[1]!=SKILL.name:errors.append('Skill name does not match directory')
    for field,limit in [('description',1024),('compatibility',500)]:
        m=re.search(r'^'+field+r': (.+)$',skill,re.M)
        if not m or not 0<len(m[1])<=limit:errors.append('Invalid frontmatter '+field)
    required=['references/style-calibration.md','references/choose.md','references/construct.md','references/fidelity.md','references/critique.md','assets/rubric.json','assets/templates/figure.json','scripts/mf.py','LICENSE','THIRD_PARTY.md']
    for name in required:
        if not (SKILL/name).is_file():errors.append('Missing installed resource: '+name)
    scanned=0
    for p in ROOT.rglob('*'):
        rel=p.relative_to(ROOT)
        if any(part in EXCLUDED for part in rel.parts) or not p.is_file():continue
        scanned+=1
        if p.is_symlink():errors.append('Repository symlink not permitted: '+str(rel))
        if p.suffix.lower() in {'.ttf','.otf','.woff','.woff2','.pem','.key'}:errors.append('Disallowed font/key asset: '+str(rel))
        if p.stat().st_size>10*1024*1024:errors.append('Oversized public file: '+str(rel))
        if p.suffix in {'.md','.json','.py','.yml','.yaml','.mjs','.html'}:
            text=p.read_text()
            if re.search(r'/Users/[A-Za-z0-9_]+/|sk-proj-[A-Za-z0-9]{10,}|github_pat_[A-Za-z0-9]{10,}',text):errors.append('Private path or credential-shaped string: '+str(rel))
            if p.suffix=='.py':
                try:ast.parse(text)
                except SyntaxError as exc:errors.append('Python syntax: '+str(rel)+' '+str(exc))
            if p.suffix=='.md':
                for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',text):
                    if target.startswith(('http://','https://','#','mailto:')):continue
                    target=target.split('#',1)[0]
                    if target and not (p.parent/target).exists():errors.append('Broken local link '+str(rel)+' -> '+target)
    return {'status':'repository_audit_pass' if not errors else 'needs_repair','files_scanned':scanned,'references':len(refs),'bundled_references':sum(bool(r['assets']) for r in refs),'image_assets':len(actual),'skill_lines':len(skill.splitlines()),'errors':errors,'notice':'Integrity and navigation checks, not a scientific or aesthetic benchmark.'}


if __name__=='__main__':
    result=audit();print(json.dumps(result,indent=2));sys.exit(0 if not result['errors'] else 2)
