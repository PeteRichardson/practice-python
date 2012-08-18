#!/usr/bin/env python

import unittest

from BankAccount import BankAccount

class BankAccountTest(unittest.TestCase):

	def testStartingBalance(self):
		self.account = BankAccount(23)
		self.assertEqual(self.account.balance, 23)

	def testDeposit(self):
		self.account = BankAccount(45)
		self.account.deposit(10)
		self.assertEqual(self.account.balance, 55)


if __name__ == "__main__":
	unittest.main()
