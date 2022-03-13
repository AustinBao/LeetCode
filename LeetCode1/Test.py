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



