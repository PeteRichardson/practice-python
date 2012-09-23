''' sell_tickets.py - semaphore example'''
import threading
import logging
from time import sleep
from random import random

logger = logging.getLogger(__name__)

tickets_left = -1


def ordinal(n):
    if 10 < n < 14: return u'%sth' % n
    if n % 10 == 1: return u'%sst' % n
    if n % 10 == 2: return u'%snd' % n
    if n % 10 == 3: return u'%srd' % n
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
                logger.info("{} sold her {} ticket.".format(self.getName(), ordinal(self.num_sold)))
                sleep(random() * 2)
            else:
                logger.info("{} is done.  No more tickets to sell.  Sold {}".format(self.getName(), self.num_sold))
                break


class Watcher(threading.Thread):
    def __init__(self, starting_tickets):
        threading.Thread.__init__(self)
        self.starting_tickets = starting_tickets

    def run(self):
        global tickets_left
        logger.info("Starting watcher")
        while True:
            if tickets_left == 0:
                break
            if (tickets_left != self.starting_tickets) and (tickets_left % 5 == 0):
                print "dump!"          
            sleep(1)
            continue


class Simulator():
    ''' Class to simulate ticket sales'''
    def __init__(self, num_tickets, num_agents):
        self.num_tickets = num_tickets
        global tickets_left
        tickets_left = self.num_tickets
        self.num_agents = num_agents
        self.agents = []
        self.watcher = Watcher(self.num_tickets)
        for which_agent in range(4):
            new_agent = Agent(name="Agent #{}".format(which_agent))
            self.agents.append(new_agent)
        logger.info("Simulation ready: {} tickets; {} agents.".format(self.num_tickets, num_agents))

    def dump(self):
        for agent in self.agents:
            logger.info("Name:  Tickets")
            logger.info("{}: {} tickets sold".format(self.getName(), ordinal(self.num_sold)))

    def start(self):
        logger.info("Simulation started.")
        self.watcher.start()
        for which_agent in range(4):
            self.agents[which_agent].start()


if __name__ == '__main__':
    FORMAT = '%(asctime)-15s %(message)s'
    logging.basicConfig(level=logging.INFO, format=FORMAT)

    sim = Simulator(num_tickets=15, num_agents=5)
    sim.start()
