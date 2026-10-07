#!/usr/bin/env python3
"""Create a deterministic, self-contained skill ZIP and SHA-256 checksum."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import zipfile
from install import SOURCE, inventory


def package(output):
    output=Path(output);output.parent.mkdir(parents=True,exist_ok=True)
    files=inventory(SOURCE)
    with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name in sorted(files):
            info=zipfile.ZipInfo('mechanism-figures/'+name,date_time=(2026,10,7,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
            z.writestr(info,(SOURCE/name).read_bytes())
        info=zipfile.ZipInfo('mechanism-figures/PACKAGE.json',date_time=(2026,10,7,0,0,0));info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
        z.writestr(info,json.dumps({'version':'0.1.0','files':files,'notice':'Original code/editorial material MIT; third-party image licenses remain separate.'},sort_keys=True,indent=2)+'\n')
    with zipfile.ZipFile(output) as z:
        broken=z.testzip()
        if broken:raise ValueError('Archive CRC failed: '+broken)
    sha=hashlib.sha256(output.read_bytes()).hexdigest()
    output.with_suffix(output.suffix+'.sha256').write_text(sha+'  '+output.name+'\n')
    return {'path':str(output),'bytes':output.stat().st_size,'sha256':sha,'files':len(files)+1}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,default=Path('.build/mechanism-figures-v0.1.0.zip'));args=parser.parse_args()
    try:print(json.dumps(package(args.output),indent=2))
    except (OSError,ValueError) as exc:print(json.dumps({'status':'packaging_failed','error':str(exc)}));sys.exit(2)
