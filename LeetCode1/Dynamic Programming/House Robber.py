import unittest
import math
from unittest import TestCase

def mostProfitFromRobbing(list_of_houses):
    previous_max_profit = 0
    current_max_profit = 0
    for money_in_house in list_of_houses:
        previous_max_profit, current_max_profit = current_max_profit, max(previous_max_profit + money_in_house, current_max_profit)
    return current_max_profit

class TestMostProfitFromRobbing(TestCase):

    def test_empty_array(self):
        houses2 = []
        self.assertEqual(first=0, second=mostProfitFromRobbing(houses2))

    def test_one_item(self):
        houses2 = [1]
        self.assertEqual(first=1, second=mostProfitFromRobbing(houses2))

    def test_two_item(self):
        houses2 = [1, 3]
        self.assertEqual(first=3, second=mostProfitFromRobbing(houses2))

    def test_spaced_apart(self):
        houses2 = [2, 1, 1, 100]
        self.assertEqual(first=102, second=mostProfitFromRobbing(houses2))


if __name__ == '__main__':
    unittest.main()
