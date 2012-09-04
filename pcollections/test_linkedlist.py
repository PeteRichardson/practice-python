#!/usr/bin/env python

import unittest
from ll import LinkedList


class LinkedListTest(unittest.TestCase):
    def test_create(self):
        list = LinkedList(50)
        self.assertEqual(None, list.next)
        self.assertEqual(50, list.value)

    def test_insert(self):
        list = LinkedList(25)
        list.insert(34)
        self.assertEqual(34, list.value)
        self.assertEqual(25, list.next.value)
        self.assertEqual(None, list.next.next)

    def test_pop(self):
        list = LinkedList(25)
        self.assertEqual(25, list.value)
        list.insert(34)
        self.assertEqual(34, list.value)
        value = list.pop()
        self.assertEqual(34, value)
        self.assertEqual(25, list.value)

    def test_append(self):
        list = LinkedList(17)
        self.assertEqual(17, list.value)
        list.append(99)
        self.assertEqual(17, list.value)
        self.assertEqual(99, list.next.value)

    def test_find(self):
        list = LinkedList(1)
        list.append(2)
        list.append(3)
        list.append(4)
        search_result = list.find(3)
        self.assertEqual(3, search_result.value)
        self.assertEqual(4, search_result.next.value)

if __name__ == "__main__":
    unittest.main()
