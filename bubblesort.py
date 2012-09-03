#!/usr/bin/env python

'''Bubblesort - O(n^2) sorting algorithm'''

import unittest
import logging
from pprint import pformat


def bubblesort(data):
    '''repeat until it's sorted
        take two elements and swap them if they're out of order'''
    if data == None or len(data) <= 1:
        return data
    else:
        swapped_one = True
        while swapped_one == True:
            logging.debug("Another pass...")
            swapped_one = False
            for item in range(0, len(data) - 1):
                logging.debug(pformat([data[item], data[item + 1]]))
                if (data[item] > data[item + 1]):
                    swapped_one = True
                    data[item], data[item + 1] = data[item + 1], data[item]
        return data


class TestBubblesort(unittest.TestCase):
    '''testcases for bubblesort routine'''

    def sort_one(self, data):
        '''compare bubblesort results with sorted() results'''
        result = bubblesort(data)
        self.assertEqual(result, sorted(data))

    def test_simple(self):
        '''sort a simple small list'''
        self.sort_one([2, 1, 3])

    def test_one(self):
        '''sort a one element list'''
        self.sort_one([1])

    def test_none(self):
        '''sort an empty list'''
        self.sort_one([])

    def test_real_None(self):
        ''' pass None to sort.  Shouldn't fail! '''
        result = bubblesort(None)
        self.assertEqual(result, None)

    def test_even(self):
        '''sort an even number of items'''
        self.sort_one([4, 3, 2, 1])

    def test_odd(self):
        '''sort an odd number of items'''
        self.sort_one([5, 4, 3, 2, 1])

if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()
