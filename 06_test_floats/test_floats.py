import pytest

def test_approx():
    assert 2.2 == pytest.approx(2.3, 0.1)
