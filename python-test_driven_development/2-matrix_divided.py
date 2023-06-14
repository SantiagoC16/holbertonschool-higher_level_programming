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

    matrix_copy = matrix.copy()
    last = -1
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix_copy, list):
        raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix_copy)):
        if last != -1 and last != len(matrix_copy[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for column in range(len(matrix_copy[row])):
            if not isinstance(matrix_copy[row][column], (int, float)):
                raise TypeError(error)
            matrix_copy[row] = list(
                map(lambda x: round((x / div), 2), matrix[row]))
    return matrix_copy
