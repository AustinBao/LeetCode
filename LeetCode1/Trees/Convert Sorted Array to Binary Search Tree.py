import unittest
from unittest import TestCase

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Code that actually turns sorted array into binary search tree
def sortedArrayToBST(nums):
    if not nums:
        return
    m = (len(nums) - 1) // 2
    root = Node(nums[m])
    root.left = sortedArrayToBST(nums[:m])
    root.right = sortedArrayToBST(nums[m + 1:])
    return root


# Code that prints out the tree (from validate binary search tree)
def isTreeLevelOrder(root):
    list_of_roots = []
    nodesPerDepth(root, 0, list_of_roots)
    return list_of_roots

def nodesPerDepth(root, depth, list_of_roots):
    if root is None:
        return
    if depth == len(list_of_roots):
        list_of_roots.append([])
    list_of_roots[depth].append(root.data)
    nodesPerDepth(root.left, depth + 1, list_of_roots)
    nodesPerDepth(root.right, depth + 1, list_of_roots)

class TestSortedAToTree(TestCase):

    def test_leetcode_example(self):
        array_values = [1, 2, 2, 3, 4, 5]
        result = isTreeLevelOrder((sortedArrayToBST(array_values)))
        self.assertEqual(first=[[2], [1, 4], [2, 3, 5]], second=result)

if __name__ == '__main__':
    unittest.main()
