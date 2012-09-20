''' threads.py - simple threading practice app'''

import threading
from time import sleep
from random import random


class Worker(threading.Thread):
    '''Some work to do in a thread'''
    MAX_SLEEP = 2

    def run(self):
        delay = random() * self.MAX_SLEEP
        sleep(delay)
        print "Hello, {}. (slept {:.2f})".format(self.getName(), delay)

if __name__ == '__main__':
    for tnum in range(4):
        Worker().start()
