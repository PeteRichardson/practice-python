''' threads.py - simple threading practice app'''

import threading
import logging

from time import sleep
from random import random
from Queue import Queue


def my_sleep(max):
    delay = random() * max
    sleep(delay)
    return delay


class Worker(threading.Thread):
    '''Some work to do in a thread'''
    MAX_SLEEP = 2

    def __init__(self, tnum, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.name = "Worker {}".format(tnum)

    def run(self):
        logger.info("Created {}".format(self.name))
        delay = 0
        if self.queue.qsize() == 0:
            logger.debug("\tqueue is empty.  Going to sleep...")
            delay = my_sleep(self.MAX_SLEEP)
        logger.debug("\twaking up after {:.2f} seconds".format(delay))
        logger.info("Hello, {}. depth: {}".format(self.name, self.queue.qsize()))

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger()

    queue = Queue()
 
    for tnum in range(4):
        t = Worker(tnum, queue)
        t.start()

    for item in range(5):
        delay = my_sleep(1)
        msg = "Hello"
        queue.put(msg)
        logger.info("Added {} to queue".format(msg))
