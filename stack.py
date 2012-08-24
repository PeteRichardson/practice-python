#!/usr/bin/env python

import unittest
from pprint import pformat
import logging

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.insert(0, item)

    def pop(self):
        answer = self.stack[0]
        self.stack = self.stack[1:]
        return answer

    def peek(self):
        return(self.stack[0])

    def count(self):
        return(len(self.stack))

    def dump(self):
        logging.debug(pformat(self.stack))


class TestStack(unittest.TestCase):
    def test_push(self):
        s = Stack()
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

if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()