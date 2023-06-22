#!/usr/bin/python3
"""task 9"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """comment"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangule__width = width
        self._Rectangule__height = height

    def area(self):
        return self._Rectangle__height * self._Rectangle__width

    def __str__(self):
        p = "[Rectangle] {}/{}"
        return p.format(self._Rectangle__width, self._Rectangle__height)
