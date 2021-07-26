import unittest
from unittest import TestCase


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = node()

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

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

    def cycle(self, index):
        # Checks if index is out of index
        if index >= self.length():
            return False
        if index < 0:
            return False
        # While loop that looks through LL for a current index that matches our given index. If yes, return true.
        curindex = 0
        curnode = self.head
        while True:
            curnode = curnode.next
            if curindex == index:
                return True
            curindex += 1

class TestCycle(TestCase):

    def test_emptylist(self):
        me = LinkedList()
        self.assertEqual(first=False, second=me.cycle(0))

    def test_indexLessThanLength(self):
        me = LinkedList()
        self.assertEqual(first=False, second=me.cycle(0))

    def test_indexGreaterThanLength(self):
        me = LinkedList()
        me.add(1)
        me.add(2)
        me.add(3)
        me.add(4)
        self.assertEqual(first=False, second=me.cycle(5))

    def test_indexInRange(self):
        me = LinkedList()
        me.add(1)
        me.add(2)
        me.add(3)
        me.add(4)
        self.assertEqual(first=True, second=me.cycle(1))

class Testlength(TestCase):

    def test_emptylist(self):
        me = LinkedList()
        self.assertEqual(first=0, second=me.length())

    def test_eleminlist(self):
        me = LinkedList()
        me.add(1)
        me.add(2)
        me.add(3)
        me.add(4)
        self.assertEqual(first=4, second=me.length())

if __name__ == '__main__':
    unittest.main()