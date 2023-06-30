#!/usr/bin/python3
"""unitest for rectangle"""
import unittest
import io
import os
import sys
from models.rectangle import Rectangle, Base


class Tests_Rectangle(unittest.TestCase):
    """test rectangle class"""

    def test_id(self):
        """test id"""
        r1 = Rectangle(1, 2, id=16)
        self.assertEqual(r1.id, 16)
        r2 = Rectangle(5, 6)
        self.assertEqual(r2.id, 1)
        r3 = Rectangle(16, 17)
        self.assertEqual(r3.id, 2)

    def test_width_height(self):
        """tests width and height and value/type error"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        with self.assertRaises(ValueError):
            r2 = Rectangle(0, 1)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 0)
        with self.assertRaises(ValueError):
            r4 = Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            r5 = Rectangle(2, -1)
        with self.assertRaises(TypeError):
            r6 = Rectangle("str", 1)
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, "str")
        with self.assertRaises(TypeError):

    def test_x_y(self):
        """tests x and y and value/type error"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 2, 3, 0)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, 0, 3)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            r5 = Rectangle(1, 2, -3, 4)
        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, 3, "str")
        with self.assertRaises(TypeError):
            r7 = Rectangle(1, 2, "str", 4)

    def test_area(self):
        """test area"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.area(), 6)
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.area(), 12)



    if __name__ == '__main__':
        unittest.main()
