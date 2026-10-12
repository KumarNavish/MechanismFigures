"""Verify skills-CLI file discovery without launching a model-backed host."""
import hashlib,json,os,subprocess,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
home=Path(os.environ['HOME'])
paths=[home/'.agents/skills/mechanism-figures',home/'.claude/skills/mechanism-figures',home/'.config/opencode/skills/mechanism-figures']
registry=json.loads((root/'assets/calibration.json').read_text())
for skill in paths:
    assert (skill/'SKILL.md').is_file(),str(skill)
    assert (skill/'SKILL.md').read_bytes()==(root/'SKILL.md').read_bytes()
    assert not (skill/'skills/mechanism-figures/SKILL.md').exists()
    for ref in registry['references']:
        for asset in ref['assets']:
            assert hashlib.sha256((skill/asset['path']).read_bytes()).hexdigest()==asset['sha256']
    r=subprocess.run([sys.executable,str(skill/'scripts/mf.py'),'references'],capture_output=True,text=True,check=True)
    assert len(json.loads(r.stdout))==20
print(json.dumps({'standard_cli_file_routes_verified':3,'references_per_install':20,'runtime_activation':'not_tested_no_agent_invoked'}))
