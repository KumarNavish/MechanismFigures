#!/usr/bin/env python3
"""Install MechanismFigures once for documented local agent hosts."""
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent/'tools'))
from global_install import main
if __name__=='__main__':sys.exit(main())
