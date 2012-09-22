''' threads.py - simple threading practice app'''

import threading
import logging

from time import sleep
from random import random
from Queue import Queue


def sleep_random(max_sleep):
    '''Sleep a random amount up to max_sleep'''
    my_delay = random() * max_sleep
    sleep(my_delay)
    return my_delay


class Worker(threading.Thread):
    '''Some work to do in a thread'''
    MAX_SLEEP = 2

    def __init__(self, thread_num, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = "Worker {}".format(thread_num)

    def run(self):
        LOGGER.info("Created {}".format(self.name))
        delay = 0
        if self.queue.qsize() == 0:
            LOGGER.debug("\tqueue is empty.  Going to sleep...")
            delay = sleep_random(self.MAX_SLEEP)
        LOGGER.debug("\t{} waking up after {:.2f} seconds".format(self.name, delay))
        LOGGER.info("Hi, {}. depth: {}".format(self.name, self.queue.qsize()))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    LOGGER = logging.getLogger()

    QUEUE = Queue()
 
    for tnum in range(4):
        t = Worker(tnum, QUEUE)
        t.start()

    for item in range(5):
        delay = sleep_random(1)
        msg = "Hello"
        QUEUE.put(msg)
        LOGGER.info("Added {} to queue".format(msg))
