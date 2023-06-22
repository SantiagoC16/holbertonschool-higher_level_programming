#!/usr/bin/python3
"""task 10"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """comment"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self._Square__size = size

    def area(self):
        return self._Square__size * self._Square__size

    def __str__(self):
        return "[Square] {}/{}".format(self._Square__size,
                                       self._Square__size)
