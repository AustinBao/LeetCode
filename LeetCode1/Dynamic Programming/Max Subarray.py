import unittest
from unittest import TestCase


def maxSubArraySum(list_of_nums):
    total_sum = max_sum = list_of_nums[0]
    for i in list_of_nums[1:]:
        total_sum = max(i, total_sum + i)
        max_sum = max(max_sum, total_sum)
    return max_sum


class TestMostProfitSubArray(TestCase):

    def test_one_item_array(self):
        list_of_nums = [0]
        self.assertEqual(first=0, second=maxSubArraySum(list_of_nums))

    def test_regular_array(self):
        self.assertEqual(first=1000, second=maxSubArraySum([0, -10, 11, -200, 1000]))


if __name__ == '__main__':
    unittest.main()
