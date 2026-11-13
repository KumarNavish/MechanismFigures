#!/usr/bin/env python3
"""Build a small zip of the skill for upload to claude.ai (Customize > Skills > Add).
Images are reduced to 1600 pixels and JPEG so that the zip stays below 10 MB. Needs Pillow.
python3 tools/pack_web.py  ->  .build/mechanism-figures-web-<version>.zip"""
import io
import json
import zipfile
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / 'VERSION').read_text().strip()
Image.MAX_IMAGE_PIXELS = None


def build():
    out = ROOT / '.build' / f'mechanism-figures-web-{VERSION}.zip'
    out.parent.mkdir(exist_ok=True)
    renamed = {}
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for p in sorted((ROOT / 'assets/calibration').iterdir()):
            im = Image.open(p).convert('RGB'); im.thumbnail((1600, 1600))
            buf = io.BytesIO(); im.save(buf, 'JPEG', quality=80, optimize=True)
            new = 'assets/calibration/' + p.stem + '.jpg'
            renamed['assets/calibration/' + p.name] = new
            z.writestr('mechanism-figures/' + new, buf.getvalue())
        files = [ROOT / n for n in ['SKILL.md', 'LICENSE', 'THIRD_PARTY.md', 'VERSION', 'assets/references.json']]
        files += [p for d in ['references', 'kit', 'scripts'] for p in sorted((ROOT / d).rglob('*')) if p.is_file() and '__pycache__' not in p.parts]
        for p in files:
            data = p.read_bytes()
            if p.suffix in {'.md', '.json'}:  # point the text at the reduced images
                text = data.decode()
                for old, new in renamed.items(): text = text.replace(old, new)
                data = text.encode()
            z.writestr('mechanism-figures/' + p.relative_to(ROOT).as_posix(), data)
    print(json.dumps({'zip': str(out.relative_to(ROOT)), 'megabytes': round(out.stat().st_size / 1e6, 2), 'images': len(renamed),
                      'note': 'Reduced images. Hashes in references.json describe the full-size files of the repository.'}))


if __name__ == '__main__':
    build()
