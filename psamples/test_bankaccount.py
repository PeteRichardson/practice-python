#!/usr/bin/env python
'''test_bankaccount.py - tests for bank account module'''

import unittest
import datetime
from bankaccount import BankAccount
from bankaccount import BankAccountHistory

class BankAccountHistoryTest(unittest.TestCase):
    '''Tests for BankAccountHistory'''

    def test_simple(self):
        self.bah = BankAccountHistory()
        self.bah.log("foo", 45.00, 45.00)
        self.assertEqual(45.00, self.bah.list[0][2])
        self.bah.log("deposit", 90.00, 135.00)
        self.assertEqual(135.00, self.bah.list[1][3])

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
