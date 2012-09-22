''' sell_tickets.py - semaphore example'''
import threading
from time import sleep
from random import random

tickets_to_sell = 15


class Agent(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.num_sold = 0

    def run(self):
        global tickets_to_sell
        while True:
            if tickets_to_sell > 0:
                tickets_to_sell -= 1
                self.num_sold += 1
                print "{} sold a ticket.  num_sold = {}.  tickets left = {}".format(self.getName(), self.num_sold, tickets_to_sell)
                sleep(random() * 2)
            else:
                break

if __name__ == '__main__':

    print "started with {} tickets to sell".format(tickets_to_sell)
    for tnum in range(4):
        t = Agent()
        t.start()
