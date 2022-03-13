import unittest
import random
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
        first_head_value = self.head
        second_head_value = llist.head
        final_list = []

        # Check if a list is empty. If it is, return the other list
        if not first_head_value.data:
            return llist
        if not second_head_value.data:
            return self
        # Set variables to nodes and compare the variable nodes value.
        if first_head_value.data <= second_head_value.data:
            smallest_temp_value = first_head_value
            first_head_value = smallest_temp_value.next
        else:
            smallest_temp_value = second_head_value
            second_head_value = smallest_temp_value.next
        final_list.append(smallest_temp_value)

        # Actually connecting and linking the nodes in the correct order
        while first_head_value and second_head_value:
            if first_head_value.data <= second_head_value.data:
                smallest_temp_value.next = first_head_value
                smallest_temp_value = first_head_value
                first_head_value = smallest_temp_value.next
                final_list.append(smallest_temp_value.data)
            else:
                smallest_temp_value.next = second_head_value
                smallest_temp_value = second_head_value
                second_head_value = smallest_temp_value.next
                final_list.append(smallest_temp_value.data)

        if first_head_value is None:
            smallest_temp_value.next = second_head_value
        if second_head_value is None:
            smallest_temp_value.next = first_head_value

        return final_list


class TestMergeSort(TestCase):

    def test_OneEmpty(self):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.add(1)
        list1.add(3)
        list1.add(6)
        list1.add(7)

        expected_merged_list = LinkedList()
        expected_merged_list.add(1)
        expected_merged_list.add(3)
        expected_merged_list.add(6)
        expected_merged_list.add(7)

        self.assertTrue(self.assert_two_lists_equal(expected_merged_list, list1.mergesorted(list2)))

    def test_SameLength(self):
        list1 = LinkedList()
        list2 = LinkedList()

        list1.add(1)
        list1.add(8)
        list1.add(5)
        list2.add(3)
        list2.add(5)
        list2.add(7)

        expected_merged_list = LinkedList()
        expected_merged_list.add(1)
        expected_merged_list.add(3)
        expected_merged_list.add(8)
        expected_merged_list.add(5)
        expected_merged_list.add(7)
        expected_merged_list.add(8)

        x = list1.mergesorted(list2)
        elems = []
        cur = x.head
        while cur.next != None:
            cur = cur.next
            elems.append(cur.data)
        print(elems)
        # self.assertTrue(1, 2, "wrong")
        self.assertTrue(self.assert_two_lists_equal(expected_merged_list, list1.mergesorted(list2)))

    def test_BigData(self):
        list1 = LinkedList()
        list2 = LinkedList()

        for i in range(1, 10000):
            list2.add(i)
            list1.add(i + i)

        list1.display()
        list2.display()

        list2.mergesorted(list1).display()

    def test_DiffLength(self):
        list1 = LinkedList()
        list2 = LinkedList()

        list1.add(1)
        list2.add(3)
        list2.add(6)
        list2.add(7)

        expected_merged_list = LinkedList()
        expected_merged_list.add(1)
        expected_merged_list.add(3)
        expected_merged_list.add(6)
        expected_merged_list.add(7)

        self.assertTrue(self.assert_two_lists_equal(expected_merged_list, list1.mergesorted(list2)))

    def test_TwoEmpty(self):
        list1 = LinkedList()
        list2 = LinkedList()

        expected_merged_list = LinkedList()

        self.assertTrue(self.assert_two_lists_equal(expected_merged_list, list1.mergesorted(list2)))

    def assert_two_lists_equal(self, list_a: LinkedList, list_b: LinkedList):
        list_a_head = list_a.head
        list_b_head = list_b.head
        while not list_a_head and list_b_head:
            if list_a_head.data != list_b_head.data:
                return False
            list_a_head = list_a_head.next
            list_b_head = list_b_head.next
        return True


if __name__ == '__main__':
    unittest.main()


