#!/usr/bin/env python

''' agent.py - something that can have a conversation'''

import threading
from random import random


class Agent(threading.Thread):
    '''something that can have a conversation'''
    phrases = ["Howdy", "Greetings.", "Yo!", "Whassup?"]

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def say_something(self):
        '''print out a random message'''
        phrase = self.phrases[int(random() * 4)]
        return "{}: {}".format(self.name, phrase)

if __name__ == "__main__":
    Pete = Agent("Pete")
    Pete.say_something()
