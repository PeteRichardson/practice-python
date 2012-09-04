#!/usr/bin/env python

import unittest
from minmax import get_minmax


class Test_minmax(unittest.TestCase):

    def test_simplemax(self):
        '''minmax - detect a simple maximum'''
        ints = [4, 5, 4]
        results = get_minmax(ints)
        self.assertEqual(results, [(1, 5, "MAX")])

    def test_simplemin(self):
        '''minmax - detect a simple minimum'''
        ints = [4, 3, 4]
        results = get_minmax(ints)
        self.assertEqual(results, [(1, 3, "MIN")])

    def test_allsame(self):
        '''minmax - detect a flat plateau'''
        ints = [4, 4, 4]
        results = get_minmax(ints)
        self.assertEqual(results, [])

    def test_allincreasing(self):
        '''minmax - detect an increasing line'''
        ints = [3, 4, 5]
        results = get_minmax(ints)
        self.assertEqual(results, [])

    def test_alldecreasing(self):
        '''minmax - detect a decreasing line'''
        ints = [5, 4, 3]
        results = get_minmax(ints)
        self.assertEqual(results, [])

    def test_complex(self):
        '''minmax - detect maxs and mins from longer sequence'''
        ints = [5, 7, 9, 8, 5, 4, 2, 1, 5, 6]
        results = get_minmax(ints)
        self.assertEqual(results, [(2, 9, "MAX"), (7, 1, "MIN")])


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()
