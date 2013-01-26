#!/usr/bin/env python

''' test_stack.py - tests for the stack class'''

import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    '''Testcases for Stack class'''
    def test_push(self):
        '''Stack - Push an item onto the stack'''
        stack = Stack()
        self.assertEqual(stack.count(), 0)
        stack.push("pete")
        topval = stack.peek()
        self.assertEqual(stack.count(), 1)
        self.assertEqual("pete", topval)

    def test_pop(self):
        '''Stack - Pop an item from the stack'''
        stack = Stack()
        stack.push("Wendy")
        stack.push("Peter")
        stack.dump()
        self.assertEqual(stack.count(), 2)
        answer = stack.pop()
        self.assertEqual(answer, "Peter")
        self.assertEqual(stack.count(), 1)

    def test_count(self):
        '''Stack - Count items on the stack'''
        stack = Stack()
        self.assertEqual(0, stack.count())
        stack.push("One")
        self.assertEqual(1, stack.count())
        stack.push("Two")
        self.assertEqual(2, stack.count())


if __name__ == "__main__":
    #import logging
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()
