#!/usr/bin/python3
"""
This module defines classes for a singly linked list with sorted insertion.

"""


class Node:
    """
    Node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Defines a singly linked list with sorted insert.
    """
    # constructor method, it initializes the linked list
    # when a new object is created, its head attribute is set to None, means the list is empty

    def __init__(self):
        # head is an instance attribute of class SinglyLinkedList. It's a pointer
        # It's a pointer to a Node object, which stores both data and a pointer to next_node
        # self.head = None represents an empty list
        self.head = None

    def sorted_insert(self, value):
        # when call Node(value), python creates a new object, value is passed to __init__ as data.
        # since we don't provide the second argument
        # therefore, self.data = value, seld.nest_node = None
        new_node = Node(value)
        # to insert a node in sorted order, need to find right position:
        # - if it's an empty list, new_node will be the head
        # - if new_node is smaller than head, set new_node to new head

        # self.head.data: the data stored in the head node of the linked list
        # self.head.next_node: the next node that the head node points to
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            # current is a local variable, it only exits inside funtion where it's defined
            # make current points to the same node as self.head
            current = self.head
            # current.next_node is not None checks if there is a next node
            # current.next_node.data is the value stored in the next node.
            # keep moveing forward, until find the first node whose value is greater than the value we want to insert.
            # insert the new_node right before it.
            while current.next_node is not None and current.next_node.data < value:
                # move current forward to next_node, now current points to where you want to insert the new node.
                current = current.next_node
            # set next_node of new node points to the node thta comes after current
            new_node.next_node = current.next_node
            # link current node to new_node, now new_node is inserted afer current, before rest of lists.
            current.next_node = new_node

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
