from typing import Counter

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    """
    Creates a node based list which contains values and references to the following node
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def to_string(self):
        current = self.head
        output_string = ''
        while current:
            output_string += '{' + str(current.value) + '} -> '
            current = current.next
        output_string = output_string + 'NULL'
        return output_string

