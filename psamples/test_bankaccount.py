#!/usr/bin/env python

import unittest

from bankaccount import BankAccount

class BankAccountTest(unittest.TestCase):
    '''Tests for BankAccount class'''

    def testStartingBalance(self):
        '''BankAccount - test starting balance'''
        self.account = BankAccount(23)
        self.assertEqual(self.account.balance, 23)

    def testDeposit(self):
        '''BankAccount - test deposit'''
        self.account = BankAccount(45)
        self.account.deposit(10)
        self.assertEqual(self.account.balance, 55)


if __name__ == "__main__":
    unittest.main()
