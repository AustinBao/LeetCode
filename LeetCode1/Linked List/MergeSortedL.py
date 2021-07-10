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

    def mergesorted(self, llist):

        list1 = self.head
        list2 = llist.head
        set = None

        # Check if a list is empty. If it is, return the other list
        if not list1:
            return list2
        if not list2:
            return list1
        # Set variables to nodes and compare the variable nodes value.
        if list1 and list2:
            if list1.data <= list2.data:
                set = list1
                list1 = set.next
            else:
                set = list2
                list2 = set.next
            newhead = set
        # Actually connecting and linking the nodes in the correct order
        while list1 and list2:
            if list1.data <= list2.data:
                set.next = list1
                set = list1
                list1 = set.next
            else:
                set.next = list2
                set = list2
                list2 = set.next
        if not list1:
            set.next = list2
        if not list2:
            set.next = list1

        return newhead


class TestMergeSort(TestCase):

    def test_OneEmpty(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.add(1)
        list1.add(3)
        list1.add(6)
        list1.add(7)
        list1.display()
        self.assertEqual(first=[1, 3, 6, 7], second=list1.mergesorted(list2))

    def test_OneShorter(self):
        lista = LinkedList()
        listb = LinkedList()
        lista.add(1)
        lista.add(3)
        lista.add(6)
        lista.add(7)
        listb.add(2)
        listb.add(3)
        lista.display()
        listb.display()
        self.assertEqual(first=[1, 2, 3, 3, 6, 7], second=lista.mergesorted(listb))


if __name__ == '__main__':
    unittest.main()


