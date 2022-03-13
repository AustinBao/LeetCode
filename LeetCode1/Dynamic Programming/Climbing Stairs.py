import unittest
import math
from unittest import TestCase


def StairCaseCases(n):
    one, two = 1, 1
    for i in range(n-1):
        temp = one
        one = one+two
        two = temp
    return one


class TestStairCase(TestCase):

    def test_zero(self):
        result = StairCaseCases(0)
        self.assertEqual(first=1, second=result)

    def test_one(self):
        result = StairCaseCases(1)
        self.assertEqual(first=1, second=result)

    def test_two(self):
        result = StairCaseCases(2)
        self.assertEqual(first=2, second=result)

    def test_three(self):
        result = StairCaseCases(3)
        self.assertEqual(first=3, second=result)

    def test_five(self):
        result = StairCaseCases(5)
        self.assertEqual(first=8, second=result)

if __name__ == '__main__':
    unittest.main()
