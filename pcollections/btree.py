#!/usr/bin/env python

''' btree.py - simple binary tree implementation'''

from pprint import pformat, pprint
from random import random as rand


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return pformat("%d" % (self.value))


class DuplicateValueException(BaseException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Duplicate Value %d" % self.value


class BTree(Node):
    def __init__(self, root):
        Node.__init__(self, root)

    def insert(self, value):
        cur = self
        if value == cur.value:
            raise DuplicateValueException(value)
        if value < cur.value:
            if cur.left is None:
                cur.left = BTree(value)
            else:
                cur.left.insert(value)
        if value > cur.value:
            if cur.right is None:
                cur.right = BTree(value)
            else:
                cur.right.insert(value)

    def dfs(self):
        cur = self
        if cur.left is not None:
            for l in cur.left.dfs():
                yield l
        yield cur
        if cur.right is not None:
            for r in cur.right.dfs():
                yield r


if __name__ == "__main__":
    bt = BTree(23)
    for r in range(1, 10):
        try:
            bt.insert(int(rand() * 50))
        except DuplicateValueException as e:
            print e
            continue

    gen = bt.dfs()
    for v in gen:
        print v
