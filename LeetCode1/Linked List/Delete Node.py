import unittest
from unittest import TestCase


class Node(object):

    def __init__(self, d, n=None):
        self.data = d
        self.next_node = n

    def get_next(self):
        return self.next_node

    def set_next(self, n):
        self.next_node = n

    def get_data(self):
        return self.data

    def set_data(self, d):
        self.data = d

    def has_next(self):
        if self.get_next() is None:
            return False
        return True

    def to_string(self):
        return "Node value: " + str(self.data)


class LinkedList(object):

    def __init__(self, r=None):
        self.root = r

    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node

    def add_node(self, n):
        n.set_next(self.root)
        self.root = n

    def remove(self, d):
        this_node = self.root
        prev_node = None

        while this_node is not None:
            if this_node.get_data() == d:
                if prev_node is not None:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                return True  # data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def print_list(self):
        print("Print List..........")
        if self.root is None:
            return
        this_node = self.root
        print(this_node.to_string())
        while this_node.has_next():
            this_node = this_node.get_next()
            print(this_node.to_string())


# How would I even write a unit test for a Linked List? I wrote a temp. variable that stored the current LL before we removed an item.
class TestDeleteNode(TestCase):

    def test_normal(self):
        myList = LinkedList()
        myList.add(5)
        myList.add(9)
        myList.add(3)
        before_deletion = myList
        myList.remove(9)
        self.assertEqual(first=myList, second=before_deletion)


if __name__ == '__main__':
    unittest.main()
