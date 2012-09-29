''' sell_tickets.py - semaphore example'''
import threading
import logging
from time import sleep
from random import random

logger = logging.getLogger(__name__)

tickets_left = -1


def ordinal(n):
    if 10 < n < 14:
        return u'%sth' % n
    if n % 10 == 1:
        return u'%sst' % n
    if n % 10 == 2:
        return u'%snd' % n
    if n % 10 == 3:
        return u'%srd' % n
    return u'%sth' % n


class Agent(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
        self.num_sold = 0

    def run(self):
        global tickets_left
        logger.info("Starting {}".format(self.getName()))
        while True:
            if tickets_left > 0:
                tickets_left -= 1
                self.num_sold += 1
                logger.debug("{} sold her {} ticket.".format(self.getName(), ordinal(self.num_sold)))
                sleep(random() * 2)
            else:
                logger.info("{} is done.  No more tickets to sell.  Sold {}".format(self.getName(), self.num_sold))
                break


class Simulator(threading.Thread):
    ''' Class to simulate ticket sales'''
    def __init__(self, starting_tickets, num_agents):
        threading.Thread.__init__(self)
        self.starting_tickets = starting_tickets
        global tickets_left
        tickets_left = self.starting_tickets
        self.num_agents = num_agents
        self.agents = []
        for which_agent in range(self.num_agents):
            new_agent = Agent(name="Agent #{}".format(which_agent))
            self.agents.append(new_agent)
        logger.info("Simulation ready: {} tickets; {} agents.".format(self.starting_tickets, num_agents))

    def dump(self):
        logger.info("{:10s}{:12s}".format("Name", "Tickets Sold"))
        logger.info("{:10s}{:12s}".format("----", "------------"))
        for agent in self.agents:
            logger.info("{:10s}{:12d}".format(agent.getName(), agent.num_sold))
        logger.info("")

    def run(self):
        logger.info("Simulation started.")
        for which_agent in range(self.num_agents):
            self.agents[which_agent].start()
        while True:
            if tickets_left == 0:
                break
            if (tickets_left != self.starting_tickets) and (tickets_left % 5 == 0):
                self.dump()
            sleep(1)
            continue



if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    sim = Simulator(starting_tickets=40, num_agents=5)
    sim.start()
