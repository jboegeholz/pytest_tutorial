import pytest

@pytest.fixture(scope="function")
def simple_fixture():
    return 42

def test_function(simple_fixture):
    assert simple_fixture == 42


