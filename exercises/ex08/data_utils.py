"""Dictionary related utility functions."""


__author__ = "730557095"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Function reads every line from filename into a list of strs."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)

    for line in csv_reader:
        file_handle.append(line)

    file_handle.close()
    return result 


def column_values(rows: list[dict[str, str]], key: str) -> list[str]:
    """Function results in list of strings of the values in a column."""
    result: list[str] = ()
    for i in rows:
        j: str = i[key]
        result.append(j)
    return result


def columnar(table_row: list[dict[str, str]]) -> dict[str, list[str]]:
    """Function results a dictionary from a table represented a list of rows."""
    result: dict[str, list[str]] = {}
    first: dict[str, str] = table_row[0]
    for key in first:
        result[key] = column_values(table_row, key)
    return result


def head(table_col: dict[str, list[str]], row_len: int) -> dict[str, list[str]]:
    """Function results a dictionary from a dictionary column and row of integers."""
    result: dict[str, list[str]] = {}
    for key in table_col:
        n_val: list[str] = []
        i: int = 0
        while i < len(table_col[key]) and i < row_len:
            n_val.append(table_col[key][i])
            i += 1
        result[key] = n_val
    return result


def select(table_col: dict[str, list[str]], name_col: list[str]) -> dict[str, list[str]]:
    """Function results a dictionary from a dictionary and list of strings."""
    result: dict[str, list[str]] = {}
    for key in name_col:
        result[key] = table_col[key]
    return result


def concat(dict_one: dict[str, list[str]], dict_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Function results a dictionary from two dictionaries and a list of strings."""
    result: dict[str, int] = {}
    for key in dict_one:
        result[key] = dict_one[key]
    for key in dict_two:
        if key in result: 
            for j in dict_two[key]:
                result[key].append(j)
        else:
            result[key] = dict_two[key]
    return result


def count(frequency: list[str]) -> dict[str, int]:
    """Function results a dictionary from a list of strings."""
    result: dict[str, int] = {}
    for key in frequency:
        if key in result:
            result[key] += 1
        else: 
            result[key] = 1
    return result