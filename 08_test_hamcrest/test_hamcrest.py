from hamcrest import assert_that, has_items
from collections.abc import Sequence


def test_compare_list_of_items():
    actual_list_of_items: Sequence[str] = ['apple', 'banana', 'cherry']
    expected_list_of_items = ['apple', 'banana']

    assert_that(actual_list_of_items, has_items(*expected_list_of_items))
