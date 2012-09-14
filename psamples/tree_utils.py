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

    def d2(self):
        if self.left == None and self.right == None:
            return 1
        elif self.left == None and self.right != None:
            return depth(self.right) + 1
        elif self.left != None and self.right == None:
            return depth(self.left) + 1
        else:
            return max(depth(self.left), depth(self.right)) + 1

    def d3(self):
        dleft = 0 if self.left == None else self.left.d3()
        dright = 0 if self.right == None else self.right.d3()
        return max(dleft, dright) + 1

    def is_balanced(self):
        dleft = self.left.d3() if self.left != None else 0
        dright = self.right.d3() if self.right != None else 0
        return abs(dleft - dright) <= 1
