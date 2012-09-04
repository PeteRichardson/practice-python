#!/usr/bin/env python

class BankAccount:
	def __init__(self, starting_balance):
		self.balance = starting_balance

	def balance(self):
		return self.balance

	def deposit(self, deposit):
		if deposit < 0:
			raise "bad deposit"
		self.balance = self.balance + deposit
