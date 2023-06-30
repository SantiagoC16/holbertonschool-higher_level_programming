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
        self.assertEqual(r2.id, 10)
        r3 = Rectangle(16, 17)
        self.assertEqual(r3.id, 11)

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

    def test_xy(self):
        """tests x and y and value/type error"""
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        with self.assertRaises(ValueError):
            r3 = Rectangle(1, 2, 3, -4)
        with self.assertRaises(ValueError):
            r4 = Rectangle(1, 2, -3, 4)
        with self.assertRaises(TypeError):
            r5 = Rectangle(1, 2, 3, "str")
        with self.assertRaises(TypeError):
            r6 = Rectangle(1, 2, "str", 4)

    def test_area(self):
        """test area"""
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.area(), 2)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.area(), 6)
        r3 = Rectangle(3, 4)
        self.assertEqual(r3.area(), 12)

    def test_str(self):
        """test str"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_display(self):
        """test display"""
        r1 = Rectangle(1, 2)
        output = io.StringIO()
        sys.stdout = output
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#\n#\n")
        r2 = Rectangle(2, 3)
        output = io.StringIO()
        sys.stdout = output
        r2.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n##\n")
        r3 = Rectangle(1, 2, 1, 2)
        output = io.StringIO()
        sys.stdout = output
        r3.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n #\n #\n")

    def test_to_dictionary(self):
        """test to_dictionary"""
        dic = {'y': 1, 'x': 2, 'id': 3, 'width': 4, 'height': 5}
        r1 = Rectangle(4, 5, 2, 1, 3)
        self.assertEqual(r1.to_dictionary(), dic)

    def test_update(self):
        """test update"""
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(5)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 10/10 - 10/10")
        r1.update(5, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 10/10 - 4/10")
        r1.update(5, 4, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 10/10 - 4/3")
        r1.update(5, 4, 3, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 2/10 - 4/3")
        r1.update(5, 4, 3, 2, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 2/1 - 4/3")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (5) 1/3 - 4/2")

    def test_create(self):
        """test create"""
        dic = {'y': 1, 'x': 2, 'id': 3, 'width': 4, 'height': 5}
        r1 = Rectangle.create(**dic)
        self.assertEqual(r1.__str__(), "[Rectangle] (3) 2/1 - 4/5")

    def test_save_to_file(self):
        """test save to file"""
        r1 = Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        os.remove("./Rectangle.json")
        r1 = Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])
        os.remove("./Rectangle.json")
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), list_rectangles_output[0].__str__())
        self.assertEqual(r2.__str__(), list_rectangles_output[1].__str__())
        os.remove("./Rectangle.json")
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), list_rectangles_output[0].__str__())
        self.assertEqual(r2.__str__(), list_rectangles_output[1].__str__())
        os.remove("./Rectangle.json")

    def test_load_from_file(self):
        """test load from file"""
        r1 = Rectangle.save_to_file(None)
        self.assertEqual(Rectangle.load_from_file(), [])
        os.remove("./Rectangle.json")
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(r1.__str__(), list_rectangles_output[0].__str__())
        self.assertEqual(r2.__str__(), list_rectangles_output[1].__str__())
        os.remove("./Rectangle.json")

    if __name__ == '__main__':
        unittest.main()
