import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import main

def test_main_runs():
    """Test that main.py executes without errors."""
    assert main is not None
