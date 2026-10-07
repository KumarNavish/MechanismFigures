#!/usr/bin/env python3
"""Build an authored motion explanation using only approved, unchanged image assets."""
from __future__ import annotations
import hashlib
import html
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/mechanism-figures'
VERSION='0.3.0'


def render_motion(references):
    refs={r['id']:r for r in references}
    selections={
        'dreamfusion':('dreamfusion','focused'),
        'alpha_focus':('alphafold','focused'),
        'graphcast':('graphcast','focused'),
        'cellrank':('cellrank','full'),
        'alphafold':('alphafold','full'),
        'congealing':('congealing','focused')
    }
    markup=(ROOT/'tools/motion.html').read_text()
    used=[]
    for token,(rid,kind) in selections.items():
        ref=refs[rid]
        asset=next(a for a in ref['assets'] if a['kind']==kind)
        if asset.get('origin')!='published-reference':raise ValueError('Motion may use only an approved published reference')
        if hashlib.sha256((SKILL/asset['path']).read_bytes()).hexdigest()!=asset['sha256']:raise ValueError('Reference bytes changed: '+rid)
        source=asset['path'].replace('assets/','',1)
        marker='@@'+token+'@@'
        if marker not in markup:raise ValueError('Missing motion image marker: '+marker)
        markup=markup.replace(marker,html.escape(source,quote=True))
        used.append({'reference':rid,'asset':asset['path'],'sha256':asset['sha256'],'publication':ref['source']})
    if '@@' in markup:raise ValueError('Unresolved motion marker')
    css=(ROOT/'tools/motion.css').read_text()
    js=(ROOT/'tools/motion.js').read_text()
    manifest={'version':VERSION,'duration_seconds':60,'kind':'authored editorial walkthrough, not a live agent run','image_policy':'Only unchanged approved published assets; overlays and native UI guide attention. No generated scientific reference or claimed output.','chapters':['Question','Study','Construct','Critique','Deliver','Possibilities'],'assets':used,'controls':['play-pause','replay','seek','chapters','reduced-motion','reference-selection'],'status_policy':'Release threshold is instructional policy, not a simulated scored verdict. Published targets are credited as references, not skill-generated results.'}
    (SKILL/'assets/motion-story.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return markup,css,js


def build_page(references):
    markup,css,js=render_motion(references)
    base=(ROOT/'tools/gallery.css').read_text()
    page='<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="color-scheme" content="light"><meta name="description" content="Watch how MechanismFigures turns a scientific question into a reference-calibrated, evidence-linked figure. A 60-second authored walkthrough using only real published images."><title>MechanismFigures — watch the workflow</title><style>'+base+'\n'+css+'</style></head><body><main class="motion-page"><div class="motion-page-bar"><a href="gallery.html">← The complete reference gallery</a><a href="https://github.com/KumarNavish/MechanismFigures">Install the skill ↗</a></div>'+markup+'</main><script>'+js+'</script></body></html>'
    (SKILL/'assets/motion.html').write_text(page)
    return markup,css,js


if __name__=='__main__':
    data=json.loads((SKILL/'assets/calibration.json').read_text())
    build_page(data['references'])
    print(json.dumps({'page':'skills/mechanism-figures/assets/motion.html','duration_seconds':60,'approved_reference_assets':6,'generated_scientific_images':0}))
