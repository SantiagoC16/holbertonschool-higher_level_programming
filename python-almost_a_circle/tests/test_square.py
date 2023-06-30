#!/usr/bin/python3
"""unitest for square"""
import unittest
import os
from models.square import Square


class Tests_Square(unittest.TestCase):
    """test square class"""

    def test_id(self):
        """test id"""
        s1 = Square(1, id=1)
        self.assertEqual(s1.id, 1)
        s2 = Square(2, id=2)
        self.assertEqual(s2.id, 2)
        s3 = Square(3)
        self.assertEqual(s3.id, 28)

    def test_size(self):
        """test size"""
        s1 = Square(16)
        self.assertEqual(s1.size, 16)
        s2 = Square(2)
        self.assertEqual(s2.size, 2)
        s3 = Square(3)
        self.assertEqual(s3.size, 3)
        with self.assertRaises(TypeError):
            s4 = Square("4")
        with self.assertRaises(ValueError):
            s5 = Square(-5)

    def test_square_xy(self):
        """test square x and y"""
        s1 = Square(1)
        self.assertEqual(s1.x, 0)
        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)
        s3 = Square(1, 3, 2)
        self.assertEqual(s3.x, 3)
        with self.assertRaises(TypeError):
            s4 = Square(1, "str")
        with self.assertRaises(ValueError):
            s5 = Square(1, -2)
        s6 = Square(1, 2, 3)
        self.assertEqual(s6.y, 3)
        with self.assertRaises(ValueError):
            s7 = Square(1, 2, -3)
        with self.assertRaises(TypeError):
            s8 = Square(1, 2, "str")

    def test_str(self):
        """test str"""
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (4) 2/3 - 1")

    def test_to_dictionary(self):
        """test to_dictionary"""
        s1 = Square(10, 2, 1, 9)
        self.assertEqual
        (s1.to_dictionary(), {'x': 1, 'y': 2, 'id': 3, 'size': 4})
        s2 = Square(4, 1, 2, 3)
        self.assertEqual
        dicti = {'x': 1, 'y': 2, 'id': 3, 'size': 4}
        self.assertEqual(s2.to_dictionary(), dicti)

    def test_update(self):
        """test update"""
        s1 = Square(10, 10, 10, 10)
        s1.update(1)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 10")
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 10/10 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/10 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        s1.update(x=1, size=2, y=3, id=4)
        self.assertEqual(s1.__str__(), "[Square] (4) 1/3 - 2")

    def test_create(self):
        """test create"""
        s1 = Square(1, 2, 3, 4)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertFalse(s1 is s2)
        self.assertEqual(s1.__str__(), s2.__str__())
        with self.assertRaises(TypeError):
            s3 = Square(1, 2, 3, 4, 5)

    def test_save_to_file(self):
        """test save_to_file"""
        s1 = Square.save_to_file(None)
        self.assertEqual(s1, None)
        self.assertEqual(Square.load_from_file(), [])
        os.remove("./Square.json")
        Square.save_to_file([])
        self.assertEqual(Square.load_from_file(), [])
        os.remove("./Square.json")
        s1 = Square.save_to_file([Square(1)])
        self.assertIsInstance(Square.load_from_file()[0], Square)
        os.remove("./Square.json")

    if __name__ == '__main__':
        unittest.main()
