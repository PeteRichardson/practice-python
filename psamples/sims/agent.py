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

    def __str__(self):
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
        LOGGER.debug("created {}".format(self.name))

    def pick_greeting(self):
        '''print out a random message'''
        return self.phrases[int(random() * 4)]

    def greet(self, who):
        '''Say Hello to someone else'''
        phrase = self.pick_greeting()
        LOGGER.debug("{:5} to {:5}: {}".format(self.name, who.name, phrase))
        msg = Message(self, phrase)
        who.hear(msg)
        self.said += 1
        self.greeted.add(who)
        LOGGER.debug("greeted {}".format(who.name))

    def hear(self, message):
        '''Receive a message from someone else'''
        self.need_responses.append(message)
        self.heard += 1

    def start(self):
        '''See if anyone has greeted us.  if so, respond,
           but only once!'''
        LOGGER.debug("Started {}".format(self.name))
        while not self.is_idle():
            message = self.need_responses.pop()
            if message.agent not in self.greeted:
                self.greet(message.agent)

    def is_idle(self):
        '''Need to respond to anyone?'''
        return len(self.need_responses) == 0


class OldMan (Agent):
    ''' An old man is an agent that doesn't hear 100% of the time '''

    def __init__(self, name, pct_missed):
        Agent.__init__(self, name)
        self.pct_missed = pct_missed / 100.0
        LOGGER.debug("\tMisses {0}% of messages.".format(self.pct_missed))

    def hear(self, message):
        if random() <= self.pct_missed:
            LOGGER.debug("missed message {0}".format(message))
        else:
            Agent.hear(self, message)

if __name__ == "__main__":
    import unittest
    unittest.main("test_agent")
