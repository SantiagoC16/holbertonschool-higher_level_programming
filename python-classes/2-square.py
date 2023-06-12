#!/usr/bin/python3
"""Write a class Square that defines a square """


class Square:
    """a class define square"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError
        if size < 0:
            raise ValueError
        self.__size = size
