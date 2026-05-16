import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_main_runs():
    with patch('builtins.input', return_value='N'):
        with patch('builtins.print'):
            import main
            assert main is not None
