import sys
from pathlib import Path
from unittest.mock import MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

sys.modules['Startup'] = MagicMock()

import main

def test_main_runs():
    assert main is not None
