#!/usr/bin/python3
"""class comment followed by 2 enters"""


class Rectangle:
    """a comment followed by an enter"""

    # class variables (class attribute)
    number_of_instances = 0 # Public class attribute
    print_symbol = "#" # Public class attribute

    # public instance attribute
    def __init__(self, width=0, height=0):
        # private instance attributes
        self.width = width # Public instance attribute with getter and setter
        self.height = height # Public instance attribute with getter and setter
        Rectangle.number_of_instances += 1

    # property (getter)
    @property
    def width(self):
        return self.__width # Private instance attribute

    # setter
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value # Private instance attribute

    # property (getter)
    @property
    def height(self):
        return self.__height # Private instance attribute¿

    # setter
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value # Private instance attribute

    # public method
    def area(self):
        return self.__height * self.__width

    # public method
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        largo = self.__height * 2
        corto = self.__width * 2
        return corto + largo

    # magic method (string representation)
    def __str__(self):
        print_rect = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for j in range(self.__height):
            for k in range(self.__width):
                print_rect += str(self.print_symbol) # Public class attribute
            print_rect += "\n"
        return print_rect[:-1]

    # magic method (representation)
    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    # magic method (destructor)
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    # static method
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    # class method
    @classmethod
    def square(cls, size=0):
        return Rectangle(width=size, height=size)