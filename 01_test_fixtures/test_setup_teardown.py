import pytest

def test_setup_and_teardown():
    assert True

@pytest.fixture(autouse=True, scope="function")
def setup_and_teardown():
    print("SetUp")
    # setup code goes here
    yield
    print("TearDown")
    # teardown code goes here