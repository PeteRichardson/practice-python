#!/usr/bin/env python

from pprint import pprint
from datetime import datetime

class BankAccountHistory:
    def __init__(self):
        self.list = []

    def log(self, transaction_type, amount, newbalance, timestamp=None):
        if timestamp == None:
            timestamp = datetime.now()
        self.list.append((datetime, transaction_type, amount, newbalance))

    def __str__(self):
        pprint(self.list)

class BankAccount:
    def __init__(self, starting_balance):

        self.balance = starting_balance

    def balance(self):
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise RuntimeError("bad deposit")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise RuntimeError("bad withdrawal amount")
        self.balance -= amount


if __name__ == "__main__":
    import unittest
    unittest.main("test_bankaccount")