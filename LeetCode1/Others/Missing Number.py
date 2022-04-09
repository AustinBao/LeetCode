import unittest
from unittest import TestCase


def missingNumberInRange(nums):
    nums.sort()
    if nums[-1] < len(nums):
        return len(nums)
    for index in range(0, len(nums) + 1):
        if nums[index] != index:
            return index


class TestMissingNum(TestCase):

    def test_two_terms(self):
        list_insert = [0, 1]
        result = missingNumberInRange(list_insert)
        self.assertEqual(first=2, second=result)

    def test_multiple_terms(self):
        list_insert = [3, 0, 4, 1, 7, 2, 6]
        result = missingNumberInRange(list_insert)
        self.assertEqual(first=5, second=result)

    def test_three_term(self):
        list_insert = [3, 1, 0]
        result = missingNumberInRange(list_insert)
        self.assertEqual(first=2, second=result)


if __name__ == '__main__':
    unittest.main()
