#!/usr/bin/python3
"Defines a class Node"


class Node:
    """A Node class
    Attributes:
    data: int
    next_node: next_node"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A singly linked class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        liste = []
        pointer = self.__head
        while pointer:
            liste.append(str(pointer.data))
            pointer = pointer.next_node
        return '\n'.join(liste)

    def sorted_insert(self, value):
        newnode = Node(value)
        if self.__head is None:
            self.__head = newnode
        elif self.__head.data >= newnode.data:
            newnode.next_node = self.__head
            self.__head = newnode
            return

        temp = self.__head
        while temp:
            if temp.next_node is None:
                break
            if newnode.data > self.__head.data and \
                    temp.next_node.data > newnode.data:
                newnode.next_node = temp.next_node
                temp.next_node = newnode
                return
            temp = temp.next_node
        temp.next_node = newnode
        newnode.next_node = None
