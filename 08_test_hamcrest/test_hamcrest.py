from hamcrest import assert_that, has_items, equal_to, starts_with, has_length
from collections.abc import Sequence, Sized

def test_hamcrest_assert():
    result = 42
    assert_that(result, equal_to(42))

def test_hamcrest_starts_with():
    name = "Max Mustermann"
    assert_that(name, starts_with("Max"))

def test_hamcrest_has_length():
    items: Sized = ['apple', 'banana', 'cherry']
    assert_that(items, has_length(3))

def test_compare_list_of_items():
    actual_list_of_items: Sequence[str] = ['apple', 'banana', 'cherry']
    assert_that(actual_list_of_items, has_items("apple", "banana"))
