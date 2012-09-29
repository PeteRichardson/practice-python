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
        self.need_responses = []

    def say_something(self):
        '''print out a random message'''
        return self.phrases[int(random() * 4)]

    def say_something_to(self, who):
        who.hear(self.say_something())

    def hear(self, message):
        self.need_responses.append(message)


if __name__ == "__main__":
    pete = Agent("Pete")
    pete.say_something()
    pete.list
