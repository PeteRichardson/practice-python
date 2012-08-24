#!/usr/bin/env python

'''stack.py - a simple stack implementation'''

import unittest
from pprint import pformat
import logging
import copy


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        '''Remove the top item from the top of the stack 
           and return it'''
        answer = self.peek()
        self.stack = self.stack[1:]
        return answer

    def peek(self):
        '''Return a copy of the top item on the stack'''
        return(copy.copy(self.stack[0]))

    def count(self):
        '''Return the number of items on the stack'''
        return(len(self.stack))

    def dump(self):
        logging.debug(pformat(self.stack))


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
        self.assertEqual(s.count(), 0)
        s.push("pete")
        p = s.peek()
        self.assertEqual(s.count(), 1)
        self.assertEqual("pete", p)

    def test_pop(self):
        s = Stack()
        s.push("Wendy")
        s.push("Peter")
        s.dump()
        self.assertEqual(s.count(), 2)
        answer = s.pop()
        self.assertEqual(answer, "Peter")
        self.assertEqual(s.count(), 1)

    def test_count(self):
        s = Stack()
        self.assertEqual(0, s.count())
        s.push("One")
        self.assertEqual(1, s.count())
        s.push("Two")
        self.assertEqual(2, s.count())
        kk


if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()