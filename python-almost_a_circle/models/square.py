#!/usr/bin/python3
"""square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """comment"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """magic method str"""

        return "[square] ({}) {}/{} - {}".format(
            self.id, self.__x, self.__y, self.__width)
