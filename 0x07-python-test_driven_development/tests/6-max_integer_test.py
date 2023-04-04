#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 3, 2, 1]), 5)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 2, 4, 3, 1]), 4)

    def test_single_element_list(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_with_negative_numbers(self):
        self.assertEqual(max_integer([-2, 0, 3, -1]), 3)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.1, 2.5, 0.3]), 2.5)

    def test_not_list_argument(self):
        with self.assertRaises(TypeError):
            max_integer(5)

if __name__ == '__main__':
    unittest.main()
