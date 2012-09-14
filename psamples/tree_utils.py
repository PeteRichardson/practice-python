#!/usr/bin/env python

''' tree_utils.py - a class to check if a tree is balanced '''


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depths(self):
        ''' return tuple with the depths of all children '''
        dleft = 0 if self.left == None else self.left.depth()
        dright = 0 if self.right == None else self.right.depth()
        return (dleft, dright)

    def depth(self):
        return max(self.depths()) + 1

    def is_balanced(self):
        return abs(self.depths()[0] - self.depths()[1]) <= 1
