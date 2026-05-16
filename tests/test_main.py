import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import main

def test_main_runs():
    assert main is not None
    assert hasattr(main, 'main')
