#!/usr/bin/env python

from pprint import pformat
from datetime import datetime


class OverdrawnError(RuntimeError):
    pass


class BankAccountHistory:
    def __init__(self, starting_balance=0):
        self.list = []
        self.log("Starting Balance", starting_balance, starting_balance)

    def log(self, transaction_type, amount, newbalance, timestamp=None):
        if not timestamp:
            timestamp = datetime.now()
        self.list.append((datetime, transaction_type, amount, newbalance))

    def __str__(self):
        return pformat(self.list)


class BankAccount:
    def __init__(self, starting_balance):
        self.history = BankAccountHistory(starting_balance)
        self.balance = starting_balance

    def balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise RuntimeError("bad deposit")
        self.balance += amount
        self.history.log("Deposit", amount, self.balance)

    def withdraw(self, amount):
        if amount < 0:
            raise RuntimeError("bad withdrawal amount")
        if amount > self.balance:
            raise OverdrawnError()
        self.balance -= amount
        self.history.log("Withdraw", amount, self.balance)


def selftest(verbosity=1):
    suite = unittest.TestLoader().loadTestsFromTestCase(BankAccountTests)
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(BankAccountHistoryTests))
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


import unittest


class BankAccountHistoryTests(unittest.TestCase):
    '''Tests for BankAccountHistory'''

    def test_simple(self):
        self.bah = BankAccountHistory()
        self.bah.log("foo", 45.00, 45.00)
        self.assertEqual(45.00, self.bah.list[1][2])
        self.bah.log("deposit", 90.00, 135.00)
        self.assertEqual(135.00, self.bah.list[2][3])


class BankAccountTests(unittest.TestCase):
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
