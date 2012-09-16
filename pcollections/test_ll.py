#!/usr/bin/env python

''' lltests.py - unit tests for ll library '''

import unittest
from ll import Node, LinkedList

class NodeTests(unittest.TestCase):
	def test_simple(self):
		n = Node(15)
		self.assertEqual(15, n.value)

	def test_None(self):
		n = Node(None)
		self.assertEqual(None, n.value)


class LLTests(unittest.TestCase):

	def test_simple(self):
		l = LinkedList(25)
		self.assertEqual(l.value, 25)

	def test_insert(self):
		l = LinkedList(37)
		l.insert(45)
		self.assertEqual(45, l.value)
		self.assertEqual(37, l.next.value)
		self.assertEqual(2, l.length())

	def test_find(self):
		l = LinkedList(1)
		l.insert(2)
		l.insert(3)
		l.insert(4)
		l.insert(5)
		n = l.find(3)
		self.assertEqual(n.value, 3)
		self.assertEqual(n.next.value, 2)
		self.assertEqual(n.next.next.value,1)

	def test_findlast(self):
		l = LinkedList(1)
		l.append(2)
		l.append(3)
		l.append(4)
		l.append(5)
		n = l.find(5)
		self.assertEqual(n.value, 5)
		self.assertEqual(n.next, None)

	def test_append(self):
		l = LinkedList(1)
		l.append(2)
		l.append(3)
		l.append(4)
		l.append(5)
		n = l.find(4)
		self.assertEqual(n.value, 4)
		self.assertEqual(l.length(), 5)
		self.assertEqual(n.next.value, 5)
		self.assertEqual(n.next.next, None)

	def test_remove(self):
		l = LinkedList(1)
		l.append(2)
		l.append(3)
		l.append(4)
		l.append(5)
		l.remove(3)
		self.assertEqual(l.value, 1)
		self.assertEqual(l.next.value, 2)
		self.assertEqual(l.next.next.value, 4)
		self.assertEqual(l.length(), 4)





if __name__ == "__main__":
	unittest.main()