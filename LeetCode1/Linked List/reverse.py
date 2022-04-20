import unittest
from unittest import TestCase


class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # Function to insert a new node at the beginning
    def add(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def printList(self):
        element = []
        temp = self.head
        while (temp):
            element.append(temp.data)
            temp = temp.next
        return element


class TestReverse(TestCase):

    def test_reverse_4_length_LL(self):
        llist = LinkedList()
        llist.add(20)
        llist.add(4)
        llist.add(15)
        llist.add(85)
        llist.reverse()
        self.assertEqual(first=[20, 4, 15, 85], second=llist.printList())


