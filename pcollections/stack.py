#!/usr/bin/env python

'''stack.py - a simple stack implementation'''

from pprint import pformat
import logging
import copy

logger = logging.getLogger(__name__)


class Stack:
    '''Simple stack implementation'''
    def __init__(self):
        self.stack = []

    def push(self, item):
        '''Push an item onto the stack'''
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
        '''Dump a pretty representation of the stack'''
        logger.debug(pformat(self.stack))
