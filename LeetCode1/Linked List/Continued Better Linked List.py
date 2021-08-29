import unittest
from unittest import TestCase


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, node=Node()):
        self.head = node

    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total += 1
            cur = cur.next
        return total

    def add_data(self, data):
        self.append_node(Node(data))

    def add_node(self, node: Node):
        self.append_node(node)

    def append_node(self, node):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node

def check_if_node_exists_in_cycle(linked_list, desired_node: Node):
    seen_nodes = []
    current_node = linked_list.head
    while current_node is not None:
        if current_node in seen_nodes:
            return desired_node in get_list_values_after_specific_entry(seen_nodes, current_node)
        seen_nodes.append(current_node)
        current_node = current_node.next
    return False

def get_list_values_after_specific_entry(list_of_nodes, desired_node):
    current_index = 0
    while list_of_nodes[current_index] is not desired_node:
        current_index += 1
    list_of_values_after_specific_node = list_of_nodes[current_index:]
    return list_of_values_after_specific_node

class TestCycle(TestCase):

    def test_True_Normal_Loop(self):
        # Construct the node with data
        node_a = Node(1)
        node_b = Node(2)
        node_c = Node(3)

        # Construct a new linked list with node_a as the head
        linked_list = LinkedList(node_a)

        # Append two nodes to the linked list, without any loops
        linked_list.add_node(node_b)
        linked_list.add_node(node_c)

        # Set the next node to node_a, creating a loop
        linked_list.add_node(node_a)

        self.assertTrue(check_if_node_exists_in_cycle(linked_list, node_c))

    def test_False_Normal_Loop(self):
        node_a = Node(1)
        node_b = Node(2)
        node_c = Node(3)

        linked_list = LinkedList(node_a)

        linked_list.add_node(node_b)
        linked_list.add_node(node_c)

        linked_list.add_node(node_b)

        self.assertFalse(check_if_node_exists_in_cycle(linked_list, node_a))

    def test_No_Loop(self):
        node_a = Node(1)
        node_b = Node(2)
        node_c = Node(3)

        linked_list = LinkedList(node_a)

        linked_list.add_node(node_b)
        linked_list.add_node(node_c)

        self.assertEqual(first=False, second=check_if_node_exists_in_cycle(linked_list, node_a))

    def test_One_Node_Cycle(self):
        node_a = Node(1)

        linked_list = LinkedList(node_a)

        linked_list.add_node(node_a)

        self.assertTrue(check_if_node_exists_in_cycle(linked_list, node_a))

    def test_Empty_Linked_List(self):
        node_a = Node(None)

        linked_list = LinkedList(node_a)

        self.assertEqual(first=False, second=check_if_node_exists_in_cycle(linked_list, node_a))


if __name__ == '__main__':
    unittest.main()
