import pytest


@pytest.mark.parametrize(
    "data, expected_mean",
    [
        ([1], 1),
        ([1, 2], 1.5),
        ([1, 2, 3], 2)
    ]
)
def test_calculate_mean(data, expected_mean):
    mean = calculate_mean(data)
    assert mean == expected_mean


def calculate_mean(data):
    return sum(data) / len(data)


