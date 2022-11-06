"""Dictionary exercise test."""


__author__ = "730557095"


from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_str_len_one() -> None:
    """Invert function return correct output with a string length of one."""
    first_dictionary: dict[str, str] = {'a': 'b', 'c': 'd'}
    assert invert(first_dictionary) == {'b': 'a', 'd': 'c'}


def test_invert_str_len_two() -> None:
    """Invert function return correct output with a string length of two."""
    first_dictionary: dict[str, str] = {'aa': 'bb', 'cc': 'dd'}
    assert invert(first_dictionary) == {'bb': 'aa', 'dd': 'cc'}


def test_invert_with_no_str() -> None:
    """Invert function return correct output with empty dictionary."""
    first_dictionary: dict[str, str] = {} 
    assert invert(first_dictionary) == {} 


def test_favorite_color_three_inputs() -> None:
    """Color function return correct output with three imputs."""
    color: dict[str, str] = {'a': 'blue', 'b': 'green', 'c': 'green'}
    assert favorite_color(color) == 'green'


def test_favorite_color_four_imputs() -> None:
    """Color function return correct output with four imputs."""
    color: dict[str, str] = {'a': 'blue', 'b': 'green', 'c': 'green', 'd': 'green'}
    assert favorite_color(color) == 'green'


def test_favorite_color_no_imputs() -> None:
    """Color function return correct output with empty dictionary."""
    color: dict[str, str] = {}
    assert favorite_color(color) == ""


def test_count_list_len_three() -> None:
    """Count function return correct output with list length of 3."""
    counter: list[str] = ["green", "green", "blue"]
    assert count(counter) == {'green': 2, 'blue': 1}


def test_count_list_len_four() -> None:
    """Count function return correct output with list length of 4."""
    counter: list[str] = ["green", "green", "blue", "blue"]
    assert count(counter) == {'green': 2, 'blue': 2} 


def test_count_list_empty() -> None:
    """Count function return correct output with empty list."""
    counter: list[str] = []
    assert count(counter) == {}