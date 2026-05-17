import main
from unittest import mock

def test_main_runs():
    with mock.patch("builtins.input", return_value="Y"):
        main.main()
