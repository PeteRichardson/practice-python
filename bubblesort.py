#!/usr/bin/env python

'''Bubblesort - O(n^2) sorting algorithm'''

import unittest
import logging
from pprint import pformat


def bubblesort(data):
    # repeat until it's sorted
    #     take two elements and swap them if they're out of order
    if len(data) <= 1:
        return data
    else:
        swapped_one = True
        while swapped_one == True:
            logging.debug("Another pass...")
            swapped_one = False
            for n in range(0, len(data) - 1):
                logging.debug(pformat([data[n], data[n + 1]]))
                if (data[n] > data[n + 1]):
                    swapped_one = True
                    data[n], data[n + 1] = data[n + 1], data[n]
        return data


class test_bubblesort(unittest.TestCase):

    def sort_one(self, data):
        result = bubblesort(data)
        self.assertEqual(result, sorted(data))

    def test_simple(self):
        self.sort_one([2, 1, 3])

    def test_one(self):
        self.sort_one([1])

    def test_none(self):
        self.sort_one([])

    def test_even(self):
        self.sort_one([4, 3, 2, 1])

    def test_odd(self):
        self.sort_one([5, 4, 3, 2, 1])

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
