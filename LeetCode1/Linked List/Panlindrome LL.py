import unittest
from unittest import TestCase


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def add(self, data):
        newnode = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = newnode

    def display(self):
        elems = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)

    def palindrome(self):
        # Add all elements in a linked list to a list
        llist_values = []
        first_node = self.head
        while first_node is not None:
            llist_values.append(first_node.data)
            temp = first_node
            first_node = temp.next
        llist_values.remove(None)

        # Check if list is empty or not
        if len(llist_values) == 0:
            return "Is palindrome"

        # itterates through list to prove it is a palindrome
        j = 0
        k = -1
        for elements in llist_values:
            if llist_values[j] != llist_values[k]:
                return "Not palindrome"
            else:
                j += 1
                k -= 1
            return "Is palindrome"



class TestPalindrome(TestCase):

    def test_empty(self):
        me = LinkedList()
        self.assertEqual(first="Is palindrome", second=me.palindrome())

    def test_one(self):
        me = LinkedList()
        me.add(1)
        self.assertEqual(first="Is palindrome", second=me.palindrome())


    def test_odd(self):
        me = LinkedList()
        me.add(1)
        me.add(2)
        me.add(3)
        me.add(2)
        me.add(1)
        self.assertEqual(first="Is palindrome", second=me.palindrome())

    def test_even(self):
        me = LinkedList()
        me.add(1)
        me.add(4)
        me.add(4)
        me.add(1)
        self.assertEqual(first="Is palindrome", second=me.palindrome())

    def test_NotPalindrome(self):
        me = LinkedList()
        me.add(1)
        me.add(2)
        me.add(3)
        me.add(4)
        self.assertEqual(first="Not palindrome", second=me.palindrome())

if __name__ == '__main__':
    unittest.main()




