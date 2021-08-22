import unittest
from unittest import TestCase


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert node to tree
    def AddNode(self, data):
        if self.data is not None:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.AddNode(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.AddNode(data)
        else:
            self.data = data

    def MaxDepth(self, root, depth=0):
        # Checks if there is a root in the tree
        if root is None:
            return depth
        children = [root.left, root.right]
        children_depths = []
        for child in children:
            children_depths.append(self.MaxDepth(child, depth + 1))
        return max(children_depths)

    # Checks the number of levels the left side of the tree ends at
    # left_branch = self.MaxDepth(root.left, depth + 1)
    # Checks the number of levels the right side of the tree ends at
    # right_branch = self.MaxDepth(root.right, depth + 1)
    # Determines which side went deeper using max() function


class TestMaxDepth(TestCase):
    # A binary tree must have a root so there are no further cases where there are no roots
    def test_Tree_With_Only_Root(self):
        root_node = Node(27)
        self.assertEqual(first=1, second=root_node.MaxDepth(root_node))

    def test_Two_Level_Tree(self):
        root_node = Node(27)
        root_node.AddNode(14)
        root_node.AddNode(35)
        self.assertEqual(first=2, second=root_node.MaxDepth(root_node))

    def test_Three_Level_Tree(self):
        root_node = Node(27)
        root_node.AddNode(14)
        root_node.AddNode(35)
        root_node.AddNode(10)
        root_node.AddNode(19)
        root_node.AddNode(31)
        root_node.AddNode(42)
        self.assertEqual(first=3, second=root_node.MaxDepth(root_node))

    def test_Four_Level_Tree(self):
        root_node = Node(27)
        root_node.AddNode(14)
        root_node.AddNode(35)
        root_node.AddNode(10)
        root_node.AddNode(19)
        root_node.AddNode(31)
        root_node.AddNode(42)
        root_node.AddNode(72)
        self.assertEqual(first=4, second=root_node.MaxDepth(root_node))

    # Gives us 8 because code can't compare strings "value" like an int so it just connects them one after the other.
    def test_Four_Level_Tree_With_Strings(self):
        root_node = Node("a")
        root_node.AddNode("b")
        root_node.AddNode("c")
        root_node.AddNode("d")
        root_node.AddNode("e")
        root_node.AddNode("f")
        root_node.AddNode("g")
        root_node.AddNode("h")
        self.assertEqual(first=8, second=root_node.MaxDepth(root_node))

if __name__ == '__main__':
    unittest.main()