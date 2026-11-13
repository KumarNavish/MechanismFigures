#!/usr/bin/env python3
"""Build the atlas, the case files, the gallery and THIRD_PARTY.md from assets/references.json.
Run `python3 tools/build.py`. Run `python3 tools/build.py --check` to audit without writing."""
import hashlib
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
E = html.escape
DIM = {'3d': '3D', 'mixed': '3D and flat', 'flat': 'Flat'}


def load():
    return json.loads((ROOT / 'assets/references.json').read_text())


def audit(data):
    """Return a list of problems. An empty list means that the registry and the files agree."""
    errors, moves, seen, files = [], data['moves'], set(), set()
    for r in data['references']:
        rid = r.get('id', '?')
        if rid in seen: errors.append('duplicate id ' + rid)
        seen.add(rid)
        for key in ['label', 'title', 'paper', 'authors', 'venue', 'year', 'figure', 'source', 'mechanism', 'lesson', 'borrow', 'check', 'limit', 'approval']:
            if not r.get(key): errors.append(f'{rid}: missing {key}')
        if r.get('dim') not in DIM: errors.append(f'{rid}: dim must be one of {list(DIM)}')
        if not r.get('moves') or any(m not in moves for m in r['moves']): errors.append(f'{rid}: unknown or missing move')
        if len(r.get('trace', [])) != 3: errors.append(f'{rid}: trace must have 3 steps')
        rights = r.get('rights', {})
        if rights.get('status') not in {'bundled', 'reference-excerpt'}: errors.append(f'{rid}: unknown rights status')
        if rights.get('status') == 'bundled' and not str(rights.get('license', '')).startswith('CC-BY'): errors.append(f'{rid}: a bundled figure needs a CC BY licence')
        if not rights.get('basis_url'): errors.append(f'{rid}: missing rights basis_url')
        if not r.get('assets'): errors.append(f'{rid}: no image')
        for a in r.get('assets', []):
            p = ROOT / a['path']; files.add(p.resolve())
            if not p.is_file(): errors.append(f'{rid}: missing file {a["path"]}'); continue
            if hashlib.sha256(p.read_bytes()).hexdigest() != a['sha256']: errors.append(f'{rid}: hash mismatch {a["path"]}')
            if not a.get('note'): errors.append(f'{rid}: asset has no treatment note')
    on_disk = {p.resolve() for p in (ROOT / 'assets/calibration').iterdir() if p.is_file()}
    for p in sorted(on_disk - files): errors.append('image not in the registry: ' + p.name)
    retired = set(data.get('retired_ids', []))
    for rid in sorted(retired & seen): errors.append('retired reference is back: ' + rid)
    # Each reference ID that the guides tell the agent to study must exist.
    study = [l for l in (ROOT / 'references/moves.md').read_text().splitlines() if l.startswith('**Study.**')]
    study += [l.rsplit('|', 2)[-2] for l in (ROOT / 'SKILL.md').read_text().splitlines() if l.startswith('| ') and '`' in l.rsplit('|', 2)[-2]]
    for rid in sorted({t for l in study for t in re.findall(r'`([a-z0-9-]+)`', l)} - seen):
        errors.append('a guide names an unknown reference: ' + rid)
    return errors


def case(r, moves):
    out = [f'# {r["label"]}', '', f'**{r["title"]}**', '',
           f'{r["authors"]}. *{r["paper"]}*. {r["venue"]} {r["year"]}, {r["figure"]}. [Publication]({r["source"]})', '',
           f'**View:** {DIM[r["dim"]]} · **Moves:** {", ".join(moves[m]["name"] for m in r["moves"])}', '',
           '## Open the image', '']
    for a in r['assets']:
        out.append(f'- [`{a["path"]}`](../../{a["path"]}): {a["kind"]}. {a["note"]}')
    out += ['', 'Look at the image file. This text does not replace the look.', '',
            '## Mechanism', '', r['mechanism'], '', '## Where to look', '']
    out += [f'{i}. {t}' for i, t in enumerate(r['trace'], 1)]
    out += ['', '## Why it works', '', r['lesson'], '', '## Take this', '', r['borrow'], '',
            '## Test your figure', '', r['check'], '']
    if r.get('avoid'): out += ['## Do not copy', '', r['avoid'], '']
    out += ['## Limit', '', r['limit'], '', '## Rights', '',
            f'{r["rights"]["note"]} Status: `{r["rights"]["status"]}`' + (f', [{r["rights"]["license"]}]({r["rights"]["license_url"]})' if r['rights'].get('license_url') else '') + '.',
            f'Selection: {r["approval"]}.', '']
    return '\n'.join(out)


def atlas(data):
    refs, moves = data['references'], data['moves']
    n3 = sum(r['dim'] != 'flat' for r in refs)
    out = ['# Atlas', '', f'{len(refs)} published figures, {sum(len(r["assets"]) for r in refs)} image files. {n3} of the figures use 3D. '
           'Open the image files and look at them. Each ID has a case file in `cases/`.', '',
           '`python3 scripts/refs.py <words>` searches this atlas and prints absolute image paths.', '', '## By move', '']
    for m, v in moves.items():
        ids = [r['id'] for r in refs if m in r['moves']]
        out.append(f'- **{v["name"]}**: {v["shows"]} ' + ', '.join(f'[`{i}`](cases/{i}.md)' for i in ids))
    out += ['', '## All references', '', '| ID | The figure shows | View | Moves | First image |', '|---|---|---|---|---|']
    for r in refs:
        out.append(f'| [`{r["id"]}`](cases/{r["id"]}.md) | {r["title"]} | {DIM[r["dim"]]} | {", ".join(r["moves"])} | `{r["assets"][0]["path"]}` |')
    return '\n'.join(out) + '\n'


def third_party(data):
    out = ['# Reference figures: attribution and rights', '',
           'The MIT licence covers the code and the text of this repository only. **The reference figures are third-party material.** '
           'They are not relicensed. Each figure is here for critical study, with its source and its recorded licence.', '',
           '`bundled` means that the article page states a Creative Commons Attribution licence, which the record names. '
           '`reference-excerpt` means that the figure is included for critical reference with no claim of a general reuse licence. '
           'Check the source terms before you reuse a figure. The authors do not endorse this skill.', '']
    for r in data['references']:
        rt = r['rights']
        out += [f'## {r["label"]}', '', f'{r["authors"]}. *{r["paper"]}*. {r["venue"]} ({r["year"]}), {r["figure"]}.', '',
                f'[Publication]({r["source"]}) · [Image source]({r.get("image_source") or r["source"]}) · [Rights basis]({rt["basis_url"]})', '',
                f'**{rt["status"]}**' + (f' · [{rt["license"]}]({rt["license_url"]})' if rt.get('license_url') else '') + f'. {rt["note"]}', '']
        out += [f'- `{a["path"]}`: {a["note"]} SHA-256 `{a["sha256"]}`.' for a in r['assets']]
        out.append('')
    return '\n'.join(out).rstrip() + '\n'


def gallery(data):
    refs, moves = data['references'], data['moves']
    version = (ROOT / 'VERSION').read_text().strip()
    cards = []
    for n, r in enumerate(refs, 1):
        first = r['assets'][0]
        more = ''.join(f'<button type="button" class="thumb" data-src="{E(a["path"].replace("assets/", "", 1))}" data-cap="{E(r["label"] + " · " + a["kind"])}"><img src="{E(a["path"].replace("assets/", "", 1))}" alt="{E(r["label"] + ", " + a["kind"])}" loading="lazy"></button>' for a in r['assets'][1:])
        rt = r['rights']
        cards.append(
            f'<article id="{r["id"]}" data-moves="{" ".join(r["moves"])}" data-dim="{r["dim"]}">'
            f'<p class="meta">{n:02d} · {E(DIM[r["dim"]])} · {" · ".join(E(moves[m]["name"]) for m in r["moves"])}</p>'
            f'<h2>{E(r["title"])}</h2>'
            f'<button type="button" class="hero" data-src="{E(first["path"].replace("assets/", "", 1))}" data-cap="{E(r["label"] + " · " + r["figure"])}" aria-label="Open {E(r["label"])} at full size">'
            f'<img src="{E(first["path"].replace("assets/", "", 1))}" alt="{E(r["label"] + ". " + r["mechanism"])}" loading="{"eager" if n < 3 else "lazy"}" decoding="async"></button>'
            + (f'<div class="more">{more}</div>' if more else '') +
            '<div class="cols"><div><h3>Look</h3><ol>' + ''.join(f'<li>{E(t)}</li>' for t in r['trace']) + '</ol></div>'
            f'<div><h3>Why it works</h3><p>{E(r["lesson"])}</p><h3>Take this</h3><p>{E(r["borrow"])}</p></div></div>'
            f'<p class="limit"><b>Limit.</b> {E(r["limit"])}</p>'
            f'<p class="cite"><b>{E(r["label"])}.</b> {E(r["authors"])}, <a href="{E(r["source"])}" rel="noopener">{E(r["paper"])}</a>, {E(r["venue"])} {r["year"]}, {E(r["figure"])}. '
            + (f'<a href="{E(rt["license_url"])}" rel="noopener">{E(rt["license"])}</a>' if rt.get('license_url') else 'Excerpt for critical reference') +
            f' · <a href="../references/cases/{r["id"]}.md">case file</a></p></article>')
    chips = '<button type="button" data-move="all" aria-pressed="true">All</button><button type="button" data-move="3d" aria-pressed="false">3D only</button>' + ''.join(
        f'<button type="button" data-move="{m}" aria-pressed="false" title="{E(v["shows"])}">{E(v["name"])}</button>' for m, v in moves.items())
    n3 = sum(r['dim'] != 'flat' for r in refs)
    page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{len(refs)} published figures that show how a system works, with a three-step reading for each. The reference atlas of the MechanismFigures skill.">
<title>MechanismFigures: the atlas</title><style>{(ROOT / 'tools/gallery.css').read_text()}</style></head><body>
<a class="skip" href="#atlas">Skip to the figures</a><main>
<header class="intro"><p class="meta">MechanismFigures {version} · reference atlas</p>
<h1>See how it works.</h1>
<p class="lead">{len(refs)} published figures. Each one lets you predict what the system does next, from the picture alone. {n3} of them do it in three dimensions. Read the title, open the image, and follow the three steps.</p>
<p class="links"><a href="https://github.com/KumarNavish/MechanismFigures">Install the skill</a><a href="../SKILL.md">How the agent works</a><a href="../references/moves.md">The fifteen moves</a><a href="../THIRD_PARTY.md">Sources and rights</a></p></header>
<nav class="chips" aria-label="Filter by visual move">{chips}<span id="count" role="status"></span></nav>
<section id="atlas">{''.join(cards)}</section>
<footer><p>All images are published figures or crops of them. No image is generated. The readings are editorial and the authors do not endorse them. Figures keep the rights of their authors and publishers. <a href="../THIRD_PARTY.md">Full record</a>.</p></footer></main>
<dialog id="viewer"><form method="dialog"><span id="cap"></span><button>Close</button></form><div><img id="big" alt=""></div></dialog>
<script>{(ROOT / 'tools/gallery.js').read_text()}</script></body></html>
'''
    return page


def build(check=False):
    data = load()
    errors = audit(data)
    outputs = {ROOT / 'references/atlas.md': atlas(data), ROOT / 'THIRD_PARTY.md': third_party(data), ROOT / 'assets/gallery.html': gallery(data)}
    for r in data['references']:
        outputs[ROOT / 'references/cases' / (r['id'] + '.md')] = case(r, data['moves'])
    stale = [p for p in (ROOT / 'references/cases').glob('*.md') if p not in outputs]
    if check:
        errors += ['generated file is not current: ' + str(p.relative_to(ROOT)) for p, text in outputs.items() if not p.is_file() or p.read_text() != text]
        errors += ['stale case file: ' + p.name for p in stale]
    elif not errors:
        (ROOT / 'references/cases').mkdir(parents=True, exist_ok=True)
        for p, text in outputs.items(): p.write_text(text)
        for p in stale: p.unlink()
    print(json.dumps({'status': 'ok' if not errors else 'needs_repair', 'references': len(data['references']),
                      'images': sum(len(r['assets']) for r in data['references']),
                      'with_3d': sum(r['dim'] != 'flat' for r in data['references']), 'errors': errors}, indent=2))
    return 0 if not errors else 2


if __name__ == '__main__':
    sys.exit(build('--check' in sys.argv))
