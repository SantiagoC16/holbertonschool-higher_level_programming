#!/usr/bin/python3
"""task 5"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """comment"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self._Rectangule__width__width = width
        self._Rectangule__height= height
