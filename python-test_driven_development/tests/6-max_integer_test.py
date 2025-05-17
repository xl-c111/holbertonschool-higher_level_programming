#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_all_positive_elements_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_all_negative_elements_list(self):
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_wrong_max(self):
        self.assertNotEqual(max_integer([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
