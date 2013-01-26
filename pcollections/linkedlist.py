#!/usr/bin/env python


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        if self.value is None:
            return "None"
        else:
            return str(self.value) + " -> "


class LinkedList(Node):

    def append(self, value):
        end = self
        while end.next is not None:
            end = end.next
        end.next = Node(value)

    def insert(self, value):
        newtail = Node(self.value)
        newtail.next = self.next
        self.value = value
        self.next = newtail

    def find(self, value):
        cur = self
        if cur.value == value:
            return cur
        while cur.next is not None:
            cur = cur.next
            if cur.value == value:
                return cur
        return None

    def pop(self):
        result = self.value
        if self.next is not None:
            self.value = self.next.value
            self.next = self.next.next
        else:
            self.next = None
        return result

    def __str__(self):
        result = Node.__str__(self)
        while self.next is not None:
            result = result + self.next.__str__()
        return result
