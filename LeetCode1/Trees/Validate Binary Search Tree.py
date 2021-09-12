import unittest
from unittest import TestCase


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def ValidateTree(tree):
    right = tree.right
    left = tree.left

    if right is None and left is None:
        return True
    if right is not None and tree.data >= right.data:
        return False
    if left is not None and tree.data <= left.data:
        return False

    return ValidateTree(left) and ValidateTree(right)



# Driver Code
if __name__ == '__main__':
    root = newNode(3)
    root.left = newNode(2)
    root.right = newNode(5)

    # root.right.left.left = newNode(40)
    if ValidateTree(root):
        print("Is BST")
    else:
        print("Not a BST")


#
# class TestMaxDepth(TestCase):
#     # A binary tree must have a root so there are no further cases where there are no roots
#     def test_Tree_With_Only_Root(self):
#         root_node = Node(27)
#         self.assertEqual(first=1, second=root_node.ValidateTree(root_node))
#
#     def test_Two_Level_Tree(self):
#         root_node = Node(27)
#         root_node.AddNode(14)
#         root_node.AddNode(35)
#         self.assertEqual(first=2, second=root_node.ValidateTree(root_node))
#
#     def test_Three_Level_Tree(self):
#         root_node = Node(27)
#         root_node.AddNode(14)
#         root_node.AddNode(35)
#         root_node.AddNode(10)
#         root_node.AddNode(19)
#         root_node.AddNode(31)
#         root_node.AddNode(42)
#         self.assertEqual(first=3, second=root_node.ValidateTree(root_node))
#
#     def test_Four_Level_Tree(self):
#         root_node = Node(27)
#         root_node.AddNode(14)
#         root_node.AddNode(35)
#         root_node.AddNode(10)
#         root_node.AddNode(19)
#         root_node.AddNode(31)
#         root_node.AddNode(42)
#         root_node.AddNode(72)
#         self.assertEqual(first=4, second=root_node.ValidateTree(root_node))
#
#     # Gives us 8 because code can't compare strings "value" like an int so it just connects them one after the other.
#     def test_Four_Level_Tree_With_Strings(self):
#         root_node = Node("a")
#         root_node.AddNode("b")
#         root_node.AddNode("c")
#         root_node.AddNode("d")
#         root_node.AddNode("e")
#         root_node.AddNode("f")
#         root_node.AddNode("g")
#         root_node.AddNode("h")
#         self.assertEqual(first=8, second=root_node.ValidateTree(root_node))
#
#
# if __name__ == '__main__':
#     unittest.main()
