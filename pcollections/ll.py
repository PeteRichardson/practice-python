#!/usr/bin/env python

''' ll.py - a simple linked list implementation'''


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        result = ""
        if self.value is None:
            result = result + "None"
        else:
            result = result + str(self.value)

        if self.next is not None:
            result = result + "->"
        return result


class LinkedList(Node):
    def __init__(self, value):
        Node.__init__(self, value)

    def insert(self, value):
        newtail = Node(self.value)
        newtail.next = self.next
        self.value = value
        self.next = newtail

    def find(self, value):
        cur = self
        while cur.value != value and cur.next is not None:
            cur = cur.next
        return cur

    def append(self, value):
        end = self
        while end.next is not None:
            end = end.next
        end.next = Node(value)

    def remove(self, value):
        target = self
        while target.value != value and target.next is not None:
            prev = target
            target = target.next
        if target is not None:
            prev.next = target.next

    def length(self):
        count = 1
        cur = self
        while cur.next is not None:
            count += 1
            cur = cur.next
        return count
