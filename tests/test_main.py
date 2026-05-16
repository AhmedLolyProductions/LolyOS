import sys
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_main_runs():
    with patch('builtins.input', return_value='N'):
        import main
        assert main is not None
