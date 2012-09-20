''' threads.py - simple threading practice app'''

import threading
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

    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        delay = 0
        if self.queue.qsize() == 0:
            delay = my_sleep(self.MAX_SLEEP)
        print "Hello, {}. (slept {:.2f}, depth: {})".format(self.getName(), delay, self.queue.qsize())

if __name__ == '__main__':

    queue = Queue()
 
    for tnum in range(4):
        t = Worker(queue)
        t.start()

    for item in range(5):
        delay = my_sleep(1)
        print "Added 1"
        queue.put("Hello")
