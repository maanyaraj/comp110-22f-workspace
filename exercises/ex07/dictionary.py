"""Dictionary exercise."""


__author__ = "730557095"


def invert(first_dictionary: dict[str, str]) -> dict[str, str]:
    """Function inverts keys and values."""
    inverted_dictionary: dict[str, str] = {}
    for key in first_dictionary: 
        if first_dictionary[key] in inverted_dictionary: 
            raise KeyError("The key value needs to be unique, sorry!")
        inverted_dictionary[first_dictionary[key]] = key
    return inverted_dictionary


def favorite_color(color: dict[str, str]) -> str:
    """Function returns most common value."""
    dictionary_count: dict[str, int] = {}
    max: int = 0
    color_output: str = ""

    for key in color:
        if color[key] in dictionary_count:
            dictionary_count[color[key]] += 1
        else: 
            dictionary_count[color[key]] = 1

    for key in dictionary_count: 
        if dictionary_count[key] > max:
            max = dictionary_count[key]
            color_output = key
        
    return color_output
    

def count(counter: list[str]) -> dict[str, int]: 
    """Function counts the frequency of each value."""
    dictionary_frequency = {}
    for key in counter:
        if key in dictionary_frequency:
            dictionary_frequency[key] += 1
        else: 
            dictionary_frequency[key] = 1
    return dictionary_frequency