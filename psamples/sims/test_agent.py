#!/usr/bin/env python

'''test_conversation.py'''

import unittest
from agent import Agent, Message, OldMan
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
        phrase = chuck.pick_greeting()
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

    def test_lots_of_folks(self):
        '''Can lots of agents talk?'''
        logger.debug("test_lots_of_folks")
        names = ['Pete', 'Wendy', 'Katherine', 'Newton', 'Zoe', 'Kitty Boo-Boo']
        agents = [Agent(name) for name in names]
        agents[0].greet(agents[1])
        for agent in agents:
            logger.debug("started {}".format(agent.name))
            agent.start()


class Test_OldMan (unittest.TestCase):
    def test_deaf_oldman(self):
        ''' test 100% message loss '''
        pete = Agent('Pete')
        bob = OldMan('Bob', 100)
        for i in range(5):
            pete.greet(bob)
        self.assertEqual(0, bob.heard)

    def test_perfect_hearing_oldman(self):
        ''' test 0% message loss '''
        pete = Agent('Pete')
        bob = OldMan('Bob', 0)
        for i in range(5):
            pete.greet(bob)
        self.assertEqual(5, bob.heard)


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

if __name__ == "__main__":
    unittest.main()
