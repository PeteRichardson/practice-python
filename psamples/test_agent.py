#!/usr/bin/env python

'''test_conversation.py'''

import unittest
from agent import Agent


class Test_Agent(unittest.TestCase):

    def test_simple(self):
        '''Does the thing work at all'''
        agent = Agent("Bond")
        self.assertEqual("Bond", agent.name)

    def test_speaking(self):
        '''Can it speak?'''
        chuck = Agent("Chuck")
        phrase = chuck.say_something()
        self.assertNotEqual(0, len(phrase))

    def test_hearing(self):
        '''Can it hear?'''
        amy = Agent("Amy")
        msg = "Are you listening?"
        amy.hear(msg)
        self.assertEqual(amy.need_responses, [msg])

if __name__ == "__main__":
    unittest.main()
