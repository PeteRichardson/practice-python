#!/usr/bin/env python

'''unit tests for bubblesort'''

import unittest
from bsort import bubblesort


class Test_Bubblesort(unittest.TestCase):
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

if __name__ == "__main__":
    #import logging
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()
