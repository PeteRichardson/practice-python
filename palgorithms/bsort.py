''' bsort.py - a module to sort arrays using bubblesort '''

import logging

logger = logging.getLogger(__name__)


def bubblesort(array):
    ''' repeatedly walk the array swapping items that are
        out of order until no swaps are possible '''

    if not array or len(array) <= 1:
        return array

    array_copy = list(array)

    item_swapped = True
    while item_swapped:
        item_swapped = False
        for n in xrange(0, len(array_copy) - 1):
            if array_copy[n] > array_copy[n + 1]:
                item_swapped = True
                logger.debug("swapping {0} [{1}] with {2} [{3}]".format
                            (n, str(array_copy[n]), n + 1, str(array_copy[n + 1])))
                array_copy[n], array_copy[n + 1] = array_copy[n + 1], array_copy[n]
    return array_copy


def selftest(verbosity=1):
    suite = unittest.TestLoader().loadTestsFromTestCase(BubblesortTests)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


import unittest


class BubblesortTests(unittest.TestCase):
    '''Tests for bubblesort routine'''

    def do_one(self, array):
        '''helper function to save typing'''
        self.assertEqual(bubblesort(array), sorted(array))

    def test_simple(self):
        '''bubblesort - test_simple '''
        self.do_one([1, 5, 2])

    def test_none(self):
        '''bubblesort - test_None '''
        self.assertEqual(None, bubblesort(None))

    def test_one(self):
        '''bubblesort - test_one '''
        self.do_one([1])

    def test_odd(self):
        '''bubblesort - test_odd '''
        self.do_one([1, 5, 10])

    def test_even(self):
        '''bubblesort - test_even '''
        self.do_one([5, 2, 7, 8])

    def test_tuple(self):
        '''bubblesort - test_tuple '''
        self.do_one((3, 2, 5))

    def test_nondestructive(self):
        '''bubblesort - test_nondestructive '''
        array = [7, 9, 3, 2]
        after = bubblesort(array)
        self.assertEqual(array[0], 7)
        self.assertEqual(after, sorted(array))
