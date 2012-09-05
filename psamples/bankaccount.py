#!/usr/bin/env python

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