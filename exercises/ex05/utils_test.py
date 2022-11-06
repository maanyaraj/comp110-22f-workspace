"""Unit test for utils."""

__author__ = "730557095"


from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty_list() -> None:
    """Given no integers, does the fuction return an empty string."""
    integer_list: list[int] = []
    assert only_evens(integer_list) == []


def test_only_evens_evens_and_odds() -> None:
    """Given a list of integers, does the function only return evens."""
    integer_list: list[int] = [4, 6, 9, 11, 14]
    assert only_evens(integer_list) == [4, 6, 14]


def test_only_evens_evens() -> None:
    """Given only even integers, does the fucntion return even integers."""
    integer_list: list[int] = [2, 4, 6, 8, 10]
    assert only_evens(integer_list) == [2, 4, 6, 8, 10]


def test_concat_empty_list() -> None:
    """Give an empty list the result is the correct output."""
    list_one: list[int] = []
    list_two: list[int] = []
    assert concat(list_one, list_two) == []


def test_concat_evens_and_odds() -> None:
    """Given two lists with even and odd integers, does the function concat the lists."""
    list_one: list[int] = [1, 2, 3, 4]
    list_two: list[int] = [5, 6, 7, 8]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_different_lengths() -> None:
    """Given two lists od different lengths, does the function concat the lists."""
    list_one: list[int] = [1, 2, 3]
    list_two: list[int] = [4, 5, 6, 7]
    assert concat(list_one, list_two) == [1, 2, 3, 4, 5, 6, 7]


def test_sub_empty_list() -> None:
    """If the list is empty, the proper output is returned."""
    list_sub: list[int] = []
    start: int = 1
    end: int = 10
    assert sub(list_sub, start, end) == []


def test_sub_negative_start() -> None:
    """If the start variable is initalized as negative, the proper output is returned."""
    list_sub: list[int] = [1, 3, 5, 7, 9]
    start: int = -2
    end: int = 2 
    assert sub(list_sub, start, end) == [1, 3]


def test_sub_end_greater_start() -> None:
    """If end is initalized as greater than the length of the list, the proper output is returned."""
    list_sub: list[int] = [1, 3, 5, 7, 9]
    start: int = 1
    end: int = 10
    assert sub(list_sub, start, end) == [3, 5, 7, 9]
