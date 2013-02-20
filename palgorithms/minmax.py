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
