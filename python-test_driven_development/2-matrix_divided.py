#!/usr/bin/python3
"""task 1"""


def matrix_divided(matrix, div):
    """_summary_

    Args:
        matrix (_type_): _description_
        div (_type_): _description_

    Raises:
        TypeError: _description_
        ZeroDivisionError: _description_
        TypeError: _description_
        TypeError: _description_

    Returns:
        _type_: _description_
    """

    new_m = matrix.copy()
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(new_m, list):
        raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not new_m or not new_m[0]:
        return new_m
    lenght = len(new_m[0])
    for row in range(len(new_m)):
        if lenght != len(new_m[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for column in range(len(new_m[row])):
            if not isinstance(new_m[row][column], (int, float)):
                raise TypeError(error)
            new_m[row] = list(map(lambda x: round((x / div), 2), matrix[row]))
    return new_m
