#!/usr/bin/python3
"""unitest for base"""
import unittest
from models.base import Base


class Tests_Base(unittest.TestCase):
    """test base class"""

    def test_ID(self):
        """ test ID """
        test = Base()
        self.assertEqual(test.id, 1)
        test = Base()
        self.assertEqual(test.id, 2)
        test = Base(16)
        self.assertEqual(test.id, 16)
        test = Base(-15)
        self.assertEqual(test.id, -15)

    def test_to_json_string(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        test_str = Base.to_json_string([{"id": 16}])
        self.assertEqual(test_str, '[{"id": 16}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        dicti = Base.from_json_string('[{"id": 16}]')
        self.assertAlmostEqual(dicti, [{"id": 16}])

    if __name__ == '__main__':
        unittest.main()
