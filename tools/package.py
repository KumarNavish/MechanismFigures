#!/usr/bin/env python3
"""Build deterministic standalone-skill and portable-plugin archives, with checksums."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile
from install import SOURCE, inventory

ROOT=Path(__file__).resolve().parents[1]
VERSION=(ROOT/'VERSION').read_text().strip()


def package(output,kind='skill'):
    if kind not in {'skill','plugin'}:raise ValueError('Package kind must be skill or plugin')
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    files=inventory(SOURCE)
    prefix='mechanism-figures/' if kind=='skill' else 'mechanism-figures-plugin/skills/mechanism-figures/'
    content={prefix+name:(SOURCE/name).read_bytes() for name in files}
    if kind=='plugin':
        plugin=json.loads((ROOT/'plugin.json').read_text())
        if plugin['version']!=VERSION:raise ValueError('Plugin and package version disagree')
        for name in ['plugin.json','LICENSE','THIRD_PARTY.md']:
            content['mechanism-figures-plugin/'+name]=(ROOT/name).read_bytes()
        content['mechanism-figures-plugin/README.md']=b'# MechanismFigures plugin\n\nInstall this portable package through the host\'s supported plugin flow. Its one skill lives in skills/mechanism-figures. A local archive is not an account-wide installation or public-directory listing.\n\nSource, global local-agent installer, scope and documentation: https://github.com/KumarNavish/MechanismFigures\n\nOriginal code/commentary MIT; third-party figures retain their source-specific rights. See THIRD_PARTY.md.\n'
    manifest={'version':VERSION,'kind':kind,'files':{p:hashlib.sha256(b).hexdigest() for p,b in content.items()},'notice':'Only original code/commentary is MIT. Third-party images retain separate rights; source credits and limitations travel with the skill.'}
    top='mechanism-figures/' if kind=='skill' else 'mechanism-figures-plugin/'
    content[top+'PACKAGE.json']=(json.dumps(manifest,sort_keys=True,indent=2)+'\n').encode()
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,b in sorted(content.items()):
            info=zipfile.ZipInfo(name,date_time=(2026,10,8,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16;z.writestr(info,b)
    with zipfile.ZipFile(output) as z:
        broken=z.testzip()
        if broken:raise ValueError('Archive CRC failed: '+broken)
    sha=hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix+'.sha256').write_text(sha+'  '+output.name+'\n')
    return {'path':str(output),'kind':kind,'version':VERSION,'bytes':output.stat().st_size,'sha256':sha,'files':len(content)}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind',choices=['skill','plugin'],default='skill')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    output=args.output or Path('.build')/('mechanism-figures-'+('plugin-' if args.kind=='plugin' else '')+'v'+VERSION+'.zip')
    try:print(json.dumps(package(output,args.kind),indent=2))
    except (OSError,ValueError) as exc:print(json.dumps({'status':'packaging_failed','error':str(exc)}));sys.exit(2)
