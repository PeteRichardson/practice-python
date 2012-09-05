#!/usr/bin/env python
'''test_bankaccount.py - tests for bank account module'''

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

    def testWithdrawal(self):
        '''BankAcount - test withdrawal'''
        self.account = BankAccount(18)
        self.account.withdraw(16)
        self.assertEqual(self.account.balance, 2)


if __name__ == "__main__":
    unittest.main()
