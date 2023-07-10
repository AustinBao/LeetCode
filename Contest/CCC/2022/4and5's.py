import unittest
from unittest import TestCase


def sumOfFourAndFives(num):
    num_of_sums = 0
    max_fours = num // 4
    trials_of_four = list(range(0, max_fours + 1))
    list_remainder = []
    for number in trials_of_four:
        x = (num - (number * 4)) % 5
        if x == 0:
            num_of_sums += 1
        list_remainder.append(x)

    return num_of_sums


class TestFourAndFives(TestCase):

    def test_zero_way(self):
        self.assertEqual(first=0, second=sumOfFourAndFives(6))

    def test_one_way(self):
        self.assertEqual(first=1, second=sumOfFourAndFives(14))

    def test_two_ways(self):
        self.assertEqual(first=2, second=sumOfFourAndFives(20))

    def test_three_ways(self):
        self.assertEqual(first=3, second=sumOfFourAndFives(40))

    def test_biggest_num(self):
        self.assertEqual(first=50001, second=sumOfFourAndFives(1000000))


if __name__ == '__main__':
    unittest.main()
