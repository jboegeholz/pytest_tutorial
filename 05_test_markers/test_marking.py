import pytest
import sys

@pytest.mark.skip(reason="Feature not yet implemented")
def test_future():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="Linux only")
def test_linux_only():
    pass

@pytest.mark.xfail(reason="Bug #123")
def test_known_bug():
    pass

@pytest.mark.slow
def test_slow_test():
    pass