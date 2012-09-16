#!/usr/bin/env python

''' ll.py - a simple linked list implementation'''


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def __str__(self):
		result = ""
		if self.value == None:
			result = result + "None"
		else:
			result = result + str(self.value)

		if self.next != None:
			result = result + "->"
		return result


class LinkedList(Node):
	def __init__(self, value):
		Node.__init__(self, value)

	def insert(self, value):
		newtail = Node(self.value)
		newtail.next = self.next
		self.value = value
		self.next = newtail

	def find(self, value):
		cur = self
		while cur.value != value and cur.next != None:
			cur = cur.next
		return cur

	def append(self, value):
		end = self
		while end.next != None:
			end = end.next
		end.next = Node(value)

	def remove(self, value):
		target = self
		while target.value != value and target.next != None:
			prev = target
			target = target.next
		if target != None:
			prev.next = target.next

	def length(self):
		count = 1
		cur = self
		while cur.next != None:
			count += 1
			cur = cur.next
		return count
		