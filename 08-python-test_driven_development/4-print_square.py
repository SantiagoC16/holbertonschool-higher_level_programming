#!/usr/bin/python3
"""task 3"""


def print_square(size):
    """_summary_

    Args:
        size (_type_): _description_

    Raises:
        TypeError: _description_
        ValueError: _description_
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
