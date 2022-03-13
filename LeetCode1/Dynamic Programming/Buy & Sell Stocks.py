import unittest
from unittest import TestCase


def maxProfitFromStocks(prices):
    current_number_index = 0
    list_of_differences = []
    while current_number_index < len(prices):
        for indexs_after_current_number_index in range(current_number_index, len(prices)):
            if prices[current_number_index] < prices[indexs_after_current_number_index]:
                list_of_differences.append(prices[indexs_after_current_number_index] - prices[current_number_index])
        current_number_index += 1

    if not list_of_differences:
        return 0
    else:
        return max(list_of_differences)


class TestMaxProfitFromBuyAndSellStocks(TestCase):

    def test_no_stocks(self):
        stockpricesexample = []
        self.assertEqual(first=0, second=maxProfitFromStocks(stockpricesexample))

    def test_one_stock(self):
        stockpricesexample = [1]
        self.assertEqual(first=0, second=maxProfitFromStocks(stockpricesexample))

    def test_no_profit(self):
        stockpricesexample = [100, 9, 6, 3, 1]
        self.assertEqual(first=0, second=maxProfitFromStocks(stockpricesexample))

    def test_yes_profit(self):
        stockpricesexample = [2, 45, 99, 100]
        self.assertEqual(first=98, second=maxProfitFromStocks(stockpricesexample))


if __name__ == '__main__':
    unittest.main()
