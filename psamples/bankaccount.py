#!/usr/bin/env python

from pprint import pformat
from datetime import datetime

class BankAccountHistory:
    def __init__(self, starting_balance=0):
        self.list = []
        self.log("Starting Balance", starting_balance, starting_balance)

    def log(self, transaction_type, amount, newbalance, timestamp=None):
        if timestamp == None:
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
        self.balance -= amount
        self.history.log("Withdraw", amount, self.balance)


if __name__ == "__main__":
    import unittest
    unittest.main("test_bankaccount")