#!/usr/bin/python3

"""
This module contains function that define a square class

Function:
    size: calculate the area of a square
"""


class Node:
    """
    Represents a single node of a singly linked list.

    Private instance attribute:
       __size: integer, size of the square.

    Methods:
        def __init__(self, data, next_node=None): Constructs a Node object
        def data(self): Retrieve data
        def data(self, value): Setter method for data
        def next_node(self): Retrieve next node
        def next_node(self, value):Setter method for next node
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
    SinglyLinkedList class represents the singly linked list.

    Private instance attribute:
        head: (no setter or getter)

    Methods:
        def __init__(self): Contructs a singlylinkedlish instance
        def __str__(self): returns a string representation of the list
        def sorted_insert(self, value): inserts a new node with a given value
        """

    def __init__(self):
        """
        Constructs a singly linked list instance
        """
        self.head = None

    def __str__(self):
        """
        Returns a string representation of the list.
        """
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        nserts a new node with the given value in the correct
                sorted position in the list (increasing order).
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
