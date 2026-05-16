import sys
from pathlib import Path
from unittest.mock import patch
import io

sys.path.insert(0, str(Path(__file__).parent.parent))

def test_main_runs():
    with patch('sys.stdin', new=io.StringIO('N\n')):
        import main
        assert main is not None
