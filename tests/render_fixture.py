"""Render a tooling fixture only; never use it as positive visual calibration."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from kit import Scene
out=Path(sys.argv[1]);out.mkdir(parents=True,exist_ok=True)
s=Scene('Tooling fixture','Formal geometry fixture for capture tests, not a research result.')
s.circle('source',(140,220),35,meaning='Fixture source',evidence=['TEST_ONLY'],status='formal')
s.circle('target',(360,220),35,meaning='Fixture target',evidence=['TEST_ONLY'],status='formal')
s.anchor('out',(175,220),'source');s.anchor('in',(325,220),'target')
s.route('transfer','out','in',meaning='Declared fixture connection',evidence=['TEST_ONLY'],status='formal')
s.label('source-label',(140,280),'Source',for_mark='source',anchor='middle')
s.label('target-label',(360,280),'Target',for_mark='target',anchor='middle')
s.save(out/'figure.svg')
