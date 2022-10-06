""" running_tools tests """

from src.running_tools import __version__, __main__
from src.running_tools import running_tools


def test_version():
    """Test the version"""
    assert __version__ == "0.0.1"


def test_main():
    """Test the main"""
    assert __main__.main() == "Welcome to running tools"


def test_get_pace():
    """Test get_pace"""
    assert running_tools.get_pace(5, 20) == 4
