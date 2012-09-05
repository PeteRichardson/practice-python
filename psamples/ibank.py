#!/usr/bin/env python

'''iBank.py - interactive bank app'''

import cmd
from bankaccount import BankAccount, OverdrawnError

class IBank(cmd.Cmd):
    '''Interactive Bank Application'''

    intro = "Welcome to the iBank"
    prompt = "bank> "

    account = None

    def account_valid(self):
        return self.account != None
    
    def do_new(self, line):
        '''Create an account'''
        if self.account_valid():
            raise RuntimeError("Account already exists.")
        else:
            line = line.strip()
            initial_balance = float(line) if len(line) > 0 else 0
            print "creating new account: initial balance =", initial_balance
            self.account = BankAccount(initial_balance)

    def do_deposit(self, line):
        '''deposit some money into account'''
        if not self.account_valid():
            print "No Account set up.  Do 'new' first."
            return

        print "depositing money:", line
        amount = float(line.strip())
        self.account.deposit(amount)
 
    def do_withdraw(self, line):
        '''withdraw some money from account'''
        if not self.account_valid():
            print "No Account set up.  Do 'new' first."
            return
        try:
            print "withdrawing money:", line
            amount = float(line.strip())
            self.account.withdraw(amount)
        except OverdrawnError:
            print "Nice try.  You don't have that much in the bank.  You have: ", self.account.balance


    def do_history(self, line):
        '''dump the account history'''
        if not self.account_valid():
            print "No Account set up.  Do 'new' first."
        else:
            print self.account.history

    def do_quit(self, line):
        '''exit the program'''
        return True

    def do_EOF(self, line):
        return True

    def postloop(self):
        print

if __name__ == '__main__':
    IBank().cmdloop()
