import unittest
from unittest import TestCase


def mergeSortedArray(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    while n > 0:
        nums1[n - 1] = nums2[n - 1]
        n -= 1
    return nums1


class TestMerge(TestCase):

    def test_normal_example(self):
        array1 = [1, 2, 3, 0, 0, 0]
        array2 = [2, 5, 6]
        len_of_num1 = 3
        len_of_num2 = 3
        self.assertEqual(first=[1, 2, 2, 3, 5, 6], second=mergeSortedArray(array1, len_of_num1, array2, len_of_num2))

    def test_num1_empty(self):
        array1 = [0, 0, 0]
        array2 = [2, 4, 7]
        len_of_num1 = 0
        len_of_num2 = 3
        self.assertEqual(first=[2, 4, 7], second=mergeSortedArray(array1, len_of_num1, array2, len_of_num2))


if __name__ == '__main__':
    unittest.main()
