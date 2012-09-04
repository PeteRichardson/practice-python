#!/usr/bin/env python

import unittest
from pcollections.linkedlist import LinkedList


class LinkedListTest(unittest.TestCase):
    '''Test cases for linked lists'''
    def test_create(self):
        '''Create a simple linked list'''
        alist = LinkedList(50)
        self.assertEqual(None, alist.next)
        self.assertEqual(50, alist.value)

    def test_insert(self):
        '''Insert an item into a linked list'''
        alist = LinkedList(25)
        alist.insert(34)
        self.assertEqual(34, alist.value)
        self.assertEqual(25, alist.next.value)
        self.assertEqual(None, alist.next.next)

    def test_pop(self):
        '''Pop an item from a linked list'''
        alist = LinkedList(25)
        self.assertEqual(25, alist.value)
        alist.insert(34)
        self.assertEqual(34, alist.value)
        value = alist.pop()
        self.assertEqual(34, value)
        self.assertEqual(25, alist.value)

    def test_append(self):
        '''Append an item to a linked list'''
        alist = LinkedList(17)
        self.assertEqual(17, alist.value)
        alist.append(99)
        self.assertEqual(17, alist.value)
        self.assertEqual(99, alist.next.value)

    def test_find(self):
        '''Find an item in a linked list'''
        alist = LinkedList(1)
        alist.append(2)
        alist.append(3)
        alist.append(4)
        search_result = alist.find(3)
        self.assertEqual(3, search_result.value)
        self.assertEqual(4, search_result.next.value)

if __name__ == "__main__":
    unittest.main()
