#!/usr/bin/env python

''' agent.py - something that can have a conversation'''

import threading
from random import random
import logging

LOGGER = logging.getLogger(__name__)


class Message:
    def __init__(self, agent, message):
        self.agent = agent
        self.message = message

    def str(self):
        '''String representation of this message'''
        return "{}: {}".format(self.agent.name, self.message)


class Agent(threading.Thread):
    '''something that can have a conversation'''
    phrases = ["Howdy", "Greetings.", "Yo!", "Whassup?"]

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.need_responses = []
        self.greeted = set()
        self.heard = 0
        self.said = 0

    def say_something(self):
        '''print out a random message'''
        return self.phrases[int(random() * 4)]

    def greet(self, who):
        '''Say Hello to someone else'''
        phrase = self.say_something()
        LOGGER.debug("{:5} to {:5}: {}".format(self.name, who.name, phrase))
        msg = Message(self, phrase)
        who.hear(msg)
        self.said += 1
        self.greeted.add(who)

    def hear(self, message):
        '''Receive a message from someone else'''
        self.need_responses.append(message)
        self.heard += 1

    def start(self):
        while len(self.need_responses) > 0:
            message = self.need_responses.pop()
            if message.agent not in self.greeted:
                self.greet(message.agent)

def main():
    '''do a basic functional test'''
    pete = Agent("Pete")
    pete.say_something()


if __name__ == "__main__":
    main()