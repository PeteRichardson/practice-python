#!/usr/bin/env python
import logging
import sys

class Person:
	def __init__(self, first, last, age, gender):
		self.first = first
		self.last = last
		self.age = age
		self.gender = gender

	def __str__(self):
		return  "%s, %s: %d (%s)" % (self.last, self.first, self.age, self.gender)

	def rename(self, first, last):
		self.first = first
		self.last = last

class Woman (Person):
	def __init__(self, first, last, age):
		Person.__init__(self, first, last, age, "F")

	def __str__(self):
		return "".join((Person.__str__(self),"\tI am a woman!"))

class Man (Person):
	def __init__(self, first, last, age):
		Person.__init__(self, first, last, age, "M")

if __name__ == "__main__":
	logger = logging.getLogger("foobly")
	logger.setLevel(logging.INFO)
	logger.addHandler(logging.StreamHandler(sys.stdout))


	people = [
		Man("Pete", "Richardson", 46),
		Woman("Wendy", "Wilson", 45)
	]

	print [p.last for p in people]
	
	for p in people:
		logger.error('log: %s' % p.first)
		print p