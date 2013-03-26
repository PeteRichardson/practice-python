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


class Adder(threading.Thread):
    '''Add work to the queue'''
    def __init__(self, number, workqueue):
        threading.Thread.__init__(self)
        self.number = number
        self.workqueue = workqueue

    def run(self):
        for itemnum in xrange(self.number):
            msg = "MESSAGE{}".format(itemnum)
            self.workqueue.put(msg)
            LOGGER.info("Added {} to workqueue".format(msg))
            delay = sleep_random(.25)


class Worker(threading.Thread):
    '''Some work to do in a thread'''
    MAX_SLEEP = 2

    def __init__(self, thread_num, workqueue, should_kill_self_func):
        threading.Thread.__init__(self)
        self.workqueue = workqueue
        self.num = thread_num
        self.name = "Worker {}".format(thread_num)
        self.should_kill_self_func = should_kill_self_func
        LOGGER.info("{} Created".format(self.name))

    def run(self):
        while not(self.should_kill_self_func()):
            if self.workqueue.qsize() == 0:
                delay = sleep_random(self.MAX_SLEEP)
            else:
                message = self.workqueue.get()
                LOGGER.debug("Handling message = {}.  Queue depth: {}".format(message, self.workqueue.qsize()*"*"))
                delay = sleep_random(self.MAX_SLEEP/2)

        LOGGER.info("{} committing suicide.".format(self.name))


class ThreadPool(threading.Thread):
    def __init__(self, workqueue):
        threading.Thread.__init__(self)
        self.workers = []
        self.workqueue = workqueue
        self.should_quit = False

    def add_worker(self):
        new_worker = Worker(len(self.workers)+1, self.workqueue, self.too_many_workers)
        self.workers.append(new_worker)
        new_worker.start()

    def optimal_worker_count(self):
        qsize = self.workqueue.qsize()
        return qsize / 2 + 1 if qsize else 0

    def too_many_workers(self):
        return self.worker_count() > self.optimal_worker_count()

    def worker_count(self):
        return len(self.workers)

    def adjust_pool_size(self):
        if self.worker_count() < self.optimal_worker_count():
            self.add_worker()
        for worker in self.workers:
            if not worker.isAlive():
                self.workers.remove(worker)

    def quit(self):
        self.should_quit = True

    def run(self):
        while not self.should_quit:
            sleep(.5)
            self.adjust_pool_size()


class App(threading.Thread):
    '''monitor what's going on'''
    def __init__(self):
        threading.Thread.__init__(self)
        self.workqueue = Queue()
        self.threadpool = ThreadPool(self.workqueue)

    def time_to_quit(self, quit):
        if not self.threadpool.optimal_worker_count():
            result = quit + 1
        else:
            result = 0
        return result


    def run(self):
        self.threadpool.start()
        Adder(40, self.workqueue).start()  # add 10 items
        quit = 0
        while True:
            sleep(1)
            LOGGER.debug("HEARTBEAT: Workers: {}.        Queue depth: {}".format(self.threadpool.worker_count(), self.workqueue.qsize()*"*"))
            quit = self.time_to_quit(quit)
            if quit > 4:
                break
        self.threadpool.quit()

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    LOGGER = logging.getLogger()

    App().start()

