#!/usr/bin/env python

'''test_conversation.py'''

import unittest
from agent import Agent, Message
import logging

class Test_Message(unittest.TestCase):

    def test_simple(self):
        '''Does the thing work at all'''
        agent = Agent("Pete")
        message = Message(agent, "Greetings")
        self.assertEqual(message.agent.name, "Pete")
        self.assertEqual(message.message, "Greetings")


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

    def test_conversation(self):
        '''Can two agents talk?'''
        pete = Agent("Pete")
        wendy = Agent("Wendy")
        pete.greet(wendy)
        pete.start()
        wendy.start()
        self.assertEqual(1, pete.heard)

if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()
