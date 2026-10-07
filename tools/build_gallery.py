#!/usr/bin/env python3
"""Build the public calibration reader and concise case pages from one registry."""
from __future__ import annotations
import html
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/mechanism-figures'
E = html.escape


def case_text(r):
    t = r['transfer']
    lines = ['# ' + r['label'] + ': ' + t['move'], '',
             '{} · {} {} · {}'.format(r['authors'], r['venue'], r['year'], r['figure']),
             '', '[Publication](' + r['source'] + ') · [Original asset](' + r['imageSource'] + ')', '',
             '**Use when:** ' + t['when'], '', '## Look in this order', '']
    lines += [str(i + 1) + '. ' + s for i, s in enumerate(t['trace'])]
    lines += ['', '## Mechanism → construction → immediate insight', '',
              '**Mechanism:** ' + r['mechanism'], '', '**Construction:** ' + r['construction'], '',
              '**The eye sees:** ' + r['eye'], '', '**Why not an ordinary plot:** ' + r['stronger'], '',
              '## Recreate the explanatory operation', '', '**Replace the objects:** ' + t['map'], '',
              '**Preserve:** ' + t['keep'], '']
    lines += [str(i + 1) + '. ' + s for i, s in enumerate(t['build'])]
    lines += ['', '**Acceptance test:** ' + t['check'], '', '**Do not copy literally:** ' + t['avoid'], '',
              '**Transfer example (proposal, not a finding):** ' + t['example'], '',
              '**Scientific boundary:** ' + r['limit'], '', '## Actual images and rights', '']
    if r['assets']:
        for a in r['assets']:
            lines.append('- [' + a['kind'] + ' figure](../../' + a['path'] + ') — ' + a['treatment'])
    else:
        lines.append('Source-link-only: open the original figure above. No image is bundled, and no generated substitute is used. A text description does not count as image inspection.')
    rights = r['rights']
    lines += ['', 'Status: ' + rights['status'] + '. ' + rights['note'], '',
              'License: ' + (rights.get('license') or 'not verified for redistribution') +
              '. [Permission basis](' + rights['basis_url'] + ').', '', r['commentary_origin'], '']
    return '\n'.join(lines)


def build():
    data = json.loads((SKILL / 'assets/calibration.json').read_text())
    refs = data['references']
    index = ['# Calibration routes', '', 'Load two case files, not the full gallery. Visually inspect the actual figures.', '',
             '`python scripts/mf.py references --group structure`', '',
             '| ID | Operation to borrow | Group | Offline figure |', '|---|---|---|---|']
    third = ['# Third-party figure credits and permissions', '',
             'Original code and editorial commentary are MIT licensed. **These figures are not MIT licensed.** Their authors retain ownership; inclusion implies no endorsement. We preserve the authors, source, license link, and all crop/rasterization notes. Article/manuscript license terms and figure-specific exceptions must be reviewed for new uses.', '',
             'This is the rights-aware public edition of the 20-reference calibration set. References without verified general redistribution permission retain their complete construction guides and original-source links, but their image bytes are not included. No generated stand-ins or broken image hotlinks are used.', '',
             'License checks recorded on 2026-10-07. Attribution and license evidence are also machine-readable in `assets/calibration.json` within the installed skill.', '']
    articles = []
    groups = sorted({r['transfer']['group'] for r in refs})
    for r in refs:
        (SKILL / 'references/cases' / (r['id'] + '.md')).write_text(case_text(r))
        index.append('| [' + r['id'] + '](cases/' + r['id'] + '.md) | ' + r['transfer']['move'] + ' | ' + r['transfer']['group'] + ' | ' + ('yes' if r['assets'] else 'source link') + ' |')
        rights, t = r['rights'], r['transfer']
        third += ['## ' + r['label'], '', r['authors'] + '. *' + r['paper'] + '*. ' + r['venue'] + ' (' + str(r['year']) + '), ' + r['figure'] + '.', '',
                  '[Publication](' + r['source'] + ') · [License evidence](' + rights['basis_url'] + ')', '',
                  '**' + rights['status'] + '** — ' + rights['note'], '']
        if rights.get('license_url'): third += ['[' + rights['license'] + '](' + rights['license_url'] + ')', '']
        for a in r['assets']:
            third += ['- `' + a['path'] + '` — ' + a['treatment'] + ' SHA-256: `' + a['sha256'] + '`.']
        third += ['']
        focused = [a for a in r['assets'] if a['kind'] == 'focused']
        if focused:
            media = '<div class="images">' + ''.join('<a href="' + E(a['path'].replace('assets/', '', 1)) + '" target="_blank"><img loading="lazy" src="' + E(a['path'].replace('assets/', '', 1)) + '" alt="' + E(r['label'] + ' — ' + r['figure'] + '. ' + r['look']) + '"></a>' for a in focused) + '</div>'
        else:
            media = '<div class="source-only"><strong>Inspect the published original.</strong><p>The construction guide is included; redistribution permission for this image has not been verified for this package.</p><a href="' + E(r['imageSource']) + '" target="_blank" rel="noopener noreferrer">Open actual figure / paper ↗</a></div>'
        row = '<div class="chain">' + ''.join('<div><h4>' + a + '</h4><p>' + E(b) + '</p></div>' for a, b in [('Mechanism', r['mechanism']), ('Visual construction', r['construction']), ('The eye understands', r['eye']), ('Why not a conventional plot?', r['stronger'])]) + '</div>'
        full_links = ''.join('<a href="' + E(a['path'].replace('assets/', '', 1)) + '" target="_blank">' + E(a['kind'] + ' image') + ' ↗</a> ' for a in r['assets'])
        article = '<article id="' + r['id'] + '" data-group="' + t['group'] + '"><div class="meta">' + E(r['venue'] + ' · ' + str(r['year']) + ' · ' + r['figure']) + '</div><h2>' + E(t['move']) + '</h2><p class="when"><b>' + E(r['label']) + '.</b> ' + E(t['when']) + '</p>' + media + '<div class="look"><b>Look here</b><ol>' + ''.join('<li>' + E(s) + '</li>' for s in t['trace']) + '</ol></div>' + row + '<details><summary>Recreate this in your project</summary><p><b>Replace the objects.</b> ' + E(t['map']) + '</p><p><b>Keep the relation.</b> ' + E(t['keep']) + '</p><ol>' + ''.join('<li>' + E(s) + '</li>' for s in t['build']) + '</ol><p><b>Acceptance test.</b> ' + E(t['check']) + '</p><p><b>Do not copy literally.</b> ' + E(t['avoid']) + '</p></details><p class="boundary"><b>Scientific boundary.</b> ' + E(r['limit']) + '</p><footer><p><a href="' + E(r['source']) + '" target="_blank" rel="noopener noreferrer">' + E(r['paper']) + ' ↗</a><br>' + E(r['authors']) + '. ' + E(rights['license'] or 'Image redistribution not verified') + '.</p>' + full_links + '<details><summary>Image treatment and permission</summary><p>' + E(rights['note']) + '</p><p>' + ' '.join(E(a['treatment']) for a in r['assets']) + '</p><a href="' + E(rights['basis_url']) + '">Permission basis ↗</a>' + (' · <a href="' + E(rights['license_url']) + '">License ↗</a>' if rights['license_url'] else '') + '</details></footer></article>'
        articles.append(article)
    (SKILL / 'references/calibration-index.md').write_text('\n'.join(index) + '\n')
    third_text = '\n'.join(third).rstrip() + '\n'
    (ROOT / 'THIRD_PARTY.md').write_text(third_text)
    (SKILL / 'THIRD_PARTY.md').write_text(third_text)
    shutil.copyfile(ROOT / 'LICENSE', SKILL / 'LICENSE')
    css = '''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f6f7f3;color:#253029;font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif}main{max-width:1160px;margin:auto;padding:40px 30px 70px}h1,h2{font-family:Georgia,serif;font-weight:400;letter-spacing:-.025em}h1{font-size:54px;line-height:1.05;max-width:800px;margin:20px 0}header p{max-width:850px}a{color:#305b43;text-underline-offset:4px}.muted,.meta,footer{color:#657164;font-size:12px}.meta{text-transform:uppercase;letter-spacing:.1em}nav{display:flex;gap:10px;flex-wrap:wrap;margin:25px 0}button,input{font:inherit}button{border:1px solid #bdc9ba;padding:8px 12px;background:white;border-radius:3px;color:inherit;cursor:pointer}button[aria-pressed=true]{background:#305b43;color:white}input{width:100%;padding:12px;border:1px solid #bdc9ba;margin-bottom:18px}article{border-top:1px solid #d6ded2;padding:34px 0;margin-bottom:20px}h2{font-size:32px;margin:8px 0}h4{font-size:12px;margin:0 0 8px}.when{font-size:14px}.images{display:flex;align-items:center;justify-content:center;gap:15px;background:white;padding:22px;border:1px solid #e0e5dc}.images a{min-width:0;max-width:100%}.images img{max-width:100%;max-height:570px;object-fit:contain;display:block}.source-only{padding:25px;border-left:3px solid #9bab90;background:#edf1e8;font-size:14px}.source-only p{max-width:700px}.look{display:grid;grid-template-columns:100px 1fr;gap:14px;margin:22px 0;font-size:14px}.look ol{margin:0;padding-left:19px}.chain{display:grid;grid-template-columns:repeat(4,1fr);gap:24px}.chain p{font-size:14px;margin-top:0}details{padding:14px 0;font-size:14px}summary{cursor:pointer;font-weight:600}details p{max-width:950px}.boundary{font-size:12px;padding:13px 16px;background:#edf1e8}footer a{margin-right:13px}footer details{font-size:12px}[hidden]{display:none!important}.notice{font-size:13px;border-left:2px solid #9bab90;padding-left:15px}button:focus-visible,a:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid #678ab1;outline-offset:3px}@media(max-width:750px){main{padding:22px 17px}h1{font-size:39px}h2{font-size:27px}.chain{grid-template-columns:1fr 1fr;gap:18px}.images{padding:10px}.look{display:block}.look>b{display:block;margin-bottom:8px}nav{gap:6px}button{font-size:12px}.images img{max-height:480px}}@media print{nav,input,.source-only{display:none}article{break-inside:avoid}.images img{max-height:350px}details{display:block}.chain{grid-template-columns:repeat(4,1fr)}}'''
    filters = '<button type="button" data-filter="all" aria-pressed="true">All 20</button>' + ''.join('<button type="button" data-filter="' + g + '" aria-pressed="false">' + g.capitalize() + '</button>' for g in groups)
    script = '''let group='all';const q=document.getElementById('search');function update(){let n=0;for(const a of document.querySelectorAll('article')){a.hidden=!((group==='all'||a.dataset.group===group)&&a.textContent.toLowerCase().includes(q.value.toLowerCase()));if(!a.hidden)n++;}document.getElementById('count').textContent=n+' of 20 references';}document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{group=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(t=>t.setAttribute('aria-pressed',String(t===b)));update();}));q.addEventListener('input',update);'''
    html_text = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>MechanismFigures — visual calibration</title><style>' + css + '</style></head><body><main><header><div class="meta">MechanismFigures / calibration reader</div><h1>See the operation.<br>Borrow the construction.</h1><p>Twenty real published references. Start with the relationship your figure must reveal, not the research field or palette. Inspect two examples, then adapt their explanatory operations to your own evidence.</p><p class="notice">Public edition: ' + str(sum(bool(r['assets']) for r in refs)) + ' references have verified, bundled image assets; the others link to their actual originals. No generated substitutes, hotlink dependencies, analytics, or external scripts. Keep this HTML beside its calibration image folder, or use the downloadable skill package.</p><a href="../SKILL.md">Skill workflow</a> · <a href="../references/critique.md">Quality rubric</a><nav aria-label="Mechanism families">' + filters + '</nav><input id="search" aria-label="Search constructions" placeholder="Search: support, feedback, invariant, lineage…"><p class="muted" id="count" role="status">20 of 20 references</p></header>' + ''.join(articles) + '<p class="muted">Original figures remain the work of their authors. Editorial interpretation is by MechanismFigures, not an author endorsement. See THIRD_PARTY.md for sources, licenses and figure treatment.</p></main><script>' + script + '</script></body></html>'
    (SKILL / 'assets/gallery.html').write_text(html_text)
    print(json.dumps({'references': len(refs), 'bundled_references': sum(bool(r['assets']) for r in refs), 'image_assets': sum(len(r['assets']) for r in refs), 'gallery': 'skills/mechanism-figures/assets/gallery.html'}))


if __name__ == '__main__': build()
