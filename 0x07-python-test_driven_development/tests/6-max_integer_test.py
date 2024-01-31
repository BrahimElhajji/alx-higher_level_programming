#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def empty_list(self):
        output = max_integer([])
        self.assertIsNone(output)

    def positive_numbers(self):
        numbers = [1, 2, 3, 4, 5]
        output = max_integer(numbers)
        self.assertEqual(output, 5)

    def negative_numbers(self):
        numbers = [-5, -3, -1, -7]
        output = max_integer(numbers)
        self.assertEqual(output, -1)

    def different_numbers(self):
        numbers = [10, -2, 5, -8, 15]
        output = max_integer(numbers)
        self.assertEqual(output, 15)

    def duplicate_max_numbers(self):
        numbers = [3, 8, 5, 3, 8, 10]
        output = max_integer(numbers)
        self.assertEqual(output, 10)

    def one_element(self):
        output = max_integer([42])
        self.assertEqual(output, 42)

    def default_arg(self):
        output = max_integer()
        self.assertIsNone(output)

    def invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer(1, "lovely")


if __name__ == '__main__':
    unittest.main()
