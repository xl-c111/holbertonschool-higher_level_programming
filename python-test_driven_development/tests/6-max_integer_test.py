#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_the_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_in_the_middle(self):
        self.assertEqual(max_integer([1, 2, 5, 4, 3]), 5)

    def test_max_the_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, 2, 8]), 8)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -2]), -1)

    def test_list_of_one_number(self):
        self.assertEqual(max_integer([5]), 5)

    def test_wrong_max(self):
        self.assertNotEqual(max_integer([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
