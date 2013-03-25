#!/usr/bin/env python

''' MinMax.py - a script to print out the local mins and maxes
    from an input file of integers'''


import logging


def is_min(old_direction, new_direction):
    '''Have we changed direction and created a local min'''
    return old_direction == -1 and new_direction == 1


def is_max(old_direction, new_direction):
    '''Have we changed direction and created a local max'''
    return old_direction == 1 and new_direction == -1


def is_same(current, nextitem):
    '''Are two items the same?  Just added for consistency'''
    return current == nextitem


def get_minmax(ints):
    '''Take a list of ints and return local mins and maxes'''
    results = []
    current = ints[0]
    location = -1
    old_direction = 0

    for nextitem in ints[1:]:
        location = location + 1
        logging.debug("%3d  |  %d  | %d",
                      old_direction, current, nextitem)
        if is_same(current, nextitem):
            # don't change old direction!
            continue

        # new direction = +1, 0 or -1
        new_direction = (nextitem - current) / abs(nextitem - current)
        if is_min(old_direction, new_direction):
            results.append((location, current, "MIN"))
        elif is_max(old_direction, new_direction):
            results.append((location, current, "MAX"))

        old_direction = new_direction
        current = nextitem

    return results


def selftest(verbosity=1):
    suite = unittest.TestLoader().loadTestsFromTestCase(MinMaxTests)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)

import unittest


class MinMaxTests(unittest.TestCase):

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
