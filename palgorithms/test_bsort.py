#!/usr/bin/env python

'''unit tests for bubblesort'''

import unittest
import logging
from bsort import bubblesort


class Test_Bubblesort(unittest.TestCase):

    def do_one(self, array):
        self.assertEqual(bubblesort(array), sorted(array))


    def test_simple(self):
        ''' test_simple '''
        self.do_one([1, 5, 2])


    def test_none(self):
        ''' test_None '''
        self.assertEqual(None, bubblesort(None))


    def test_one(self):
        ''' test_one '''
        self.do_one([1])


    def test_odd(self):
        ''' test_odd '''
        self.do_one([1, 5, 10])


    def test_even(self):
        ''' test_even '''
        self.do_one([5, 2, 7, 8])


    def test_tuple(self):
        ''' test_tuple '''
        self.do_one((3, 2, 5))

 
    def test_nondestructive(self):
        ''' test_nondestructive '''
        array = [7, 9, 3, 2]
        after = bubblesort(array)
        self.assertEqual(array[0], 7)
        self.assertEqual(after, sorted(array))

if __name__ == "__main__":

    logging.basicConfig(level=logging.DEBUG)
    unittest.main()

