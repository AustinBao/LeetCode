import unittest
from unittest import TestCase

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def isTreeLevelOrder(self, root):
        self.list_of_roots = []
        self.nodesPerDepth(root, 0)
        return self.list_of_roots

    def nodesPerDepth(self, root, depth):
        if root is None:
            return
        if depth == len(self.list_of_roots):
            self.list_of_roots.append([])
        self.list_of_roots[depth].append(root.data)
        self.nodesPerDepth(root.left, depth + 1)
        self.nodesPerDepth(root.right, depth + 1)


class TestBTLevelOrderTraversal(TestCase):

    def test_one_node(self):
        Tree1 = Node(3)
        self.assertEqual(first=[[3]], second= Tree1.isTreeLevelOrder(Tree1))

    def test_leetcode_example(self):
        Tree1 = Node(3)
        Tree1.left = Node(9)
        Tree1.right = Node(20)
        Tree1.right.left = Node(15)
        Tree1.right.right = Node(7)
        self.assertEqual(first=[[3], [9,20], [15, 7]], second= Tree1.isTreeLevelOrder(Tree1))

if __name__ == '__main__':
    unittest.main()