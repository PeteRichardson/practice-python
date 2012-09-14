#!/usr/bin/env python

''' tree_utils.py - a class to check if a tree is balanced '''


def depth(node):
    ''' return depth of the tree
            depth(a single node) == 1 '''
    if node == None:
        return 0
    else:
        return max(depth(node.left), depth(node.right)) + 1

def is_balanced(n):
        return abs(depth(n.left) - depth(n.right)) <= 1


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
