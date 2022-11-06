"""EX04 Utils."""
__author__ = "730557095"


def all(integer_list: list[int], given_integer: int) -> bool: 
    """Detrmine if all numbers in list match indicated number."""
    i: int = 0 
    if len(integer_list) == 0:
        return False
    while i < len(integer_list):
        if integer_list[i] == given_integer:
            i = i + 1
        else: 
            return False 
    return True


def max(input: list[int]) -> int:
    """Give largest integer of the list."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    j: int = 0 
    higher: int = input[0]
    while j < len(input): 
        if input[j] > higher:
            higher = input[j]
        j = j + 1
    return higher


def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """Determine if lists are equal to eachother."""
    m: int = 0 
    if len(list_one) != len(list_two): 
        return False
    while m < len(list_one) and m < len(list_two):
        if list_one[m] == list_two[m]: 
            m = m + 1
        else: 
            return False
    return True