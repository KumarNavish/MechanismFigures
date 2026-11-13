#!/usr/bin/env python3
"""Find reference figures in the atlas. Prints absolute image paths: open them and look.
python3 refs.py                 list all references
python3 refs.py cutaway field   the 8 best matches for the words (a move name or an ID counts most)
python3 refs.py --moves         list the moves"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'assets/references.json').read_text())
words = [w.lower() for w in sys.argv[1:]]
if words == ['--moves']:
    for key, m in data['moves'].items(): print(f'{key:15} {m["name"]}: {m["shows"]}')
    sys.exit(0)
def score(r):
    text = json.dumps(r, ensure_ascii=False).lower()
    return sum((3 if w in r['moves'] or w == r['id'] else 1) for w in words if w in text)
hits = [r for r in data['references'] if not words or score(r)]
hits.sort(key=lambda r: (-score(r), r['dim'] == 'flat'))
if words: hits = hits[:8]
for r in hits:
    print(f'\n{r["id"]}  [{r["dim"]}; {", ".join(r["moves"])}]\n  {r["title"]}')
    for a in r['assets']: print(f'  image: {ROOT / a["path"]}')
    print(f'  case:  {ROOT / "references/cases" / (r["id"] + ".md")}')
print(f'\n{len(hits)} of {len(data["references"])} references, best match first. Open two or more of the image files before you draw.')
