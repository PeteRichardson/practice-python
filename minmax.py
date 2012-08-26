#!/usr/bin/env python

''' MinMax.py - a script to print out the local mins and maxes
    from an input file of integers'''


import logging
import unittest


def is_min(old_direction, new_direction):
    return old_direction == -1 and new_direction == 1


def is_max(old_direction, new_direction):
    return old_direction == 1 and new_direction == -1


def is_same(current, next):
    return current == next


def get_minmax(ints):
    results = []
    current = ints[0]
    location = -1
    old_direction = 0

    for next in ints[1:]:
        location = location + 1
        logging.debug("%3d  |  %d  | %d" % (old_direction, current, next))
        if is_same(current, next):
            # don't change old direction!
            continue

        # new direction = +1, 0 or -1
        new_direction = (next - current) / abs(next - current)
        if is_min(old_direction, new_direction):
            results.append((location, current, "MIN"))
        elif is_max(old_direction, new_direction):
            results.append((location, current, "MAX"))

        old_direction = new_direction
        current = next

    return results


class Test_minmax(unittest.TestCase):

    def test_simplemax(self):
        ints = [4, 5, 4]
        results = get_minmax(ints)
        self.assertEqual(results, [(1, 5, "MAX")])

    def test_simplemin(self):
        ints = [4, 3, 4]
        results = get_minmax(ints)
        self.assertEqual(results, [(1, 3, "MIN")])

    def test_allsame(self):
        ints = [4, 4, 4]
        results = get_minmax(ints)
        self.assertEqual(results, [])

    def test_allincreasing(self):
        ints = [3, 4, 5]
        results = get_minmax(ints)
        self.assertEqual(results, [])

    def test_alldecreasing(self):
        ints = [5, 4, 3]
        results = get_minmax(ints)
        self.assertEqual(results, [])

    def test_complex(self):
        ints = [5, 7, 9, 8, 5, 4, 2, 1, 5, 6]
        results = get_minmax(ints)
        self.assertEqual(results, [(2, 9, "MAX"), (7, 1, "MIN")])


if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    unittest.main()
