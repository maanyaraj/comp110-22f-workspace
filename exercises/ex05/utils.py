"""EX05 Utils."""


__author__ = "730557095"


def only_evens(integer_list: list[int]) -> list[int]: 
    """Returns even elements of the input parameter."""
    i: int = 0
    result_list: list[int] = []
    while i < len(integer_list):
        if integer_list[i] % 2 == 0: 
            result_list.append(integer_list[i])
        i += 1
    return result_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Concat both of the given lists."""
    return list_one + list_two


def sub(list_sub: list[int], start: int, end: int) -> list[int]:
    """Returns subset of the given list."""
    final_list: list[int]
    if start < 0:
        start = 0 
    if end > len(list_sub):
        end = len(list_sub)
    if len(list_sub) == 0 or end <= 0 or start > len(list_sub):
        final_list = list()
    else: 
        final_list = list_sub[start:end]
    return final_list