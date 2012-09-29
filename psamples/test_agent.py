#!/usr/bin/env python

'''test_conversation.py'''

import unittest
from agent import Agent


class Test_Agent(unittest.TestCase):

    def test_simple(self):
        '''Does the thing work at all'''
        agent = Agent("Bond")
        self.assertEqual("Bond", agent.name)

    def test_phrase(self):
        '''Can it speak?'''
        chuck = Agent("Chuck")
        speech = chuck.say_something()
        self.assertEqual("Chuck:", speech[:6])

if __name__ == "__main__":
    unittest.main()
