#!/usr/bin/env python

''' MinMax.py - a script to print out the local mins and maxes
    from an input file of integers'''


from pprint import pprint
import logging


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
        new_direction = (next - current)/abs(next - current)
        if is_min(old_direction, new_direction):
            results.append((location, current, "MIN"))
        elif is_max(old_direction, new_direction):
            results.append((location, current, "MAX"))

        old_direction = new_direction
        current = next


    return results


def read_file(fname):
    return [int(l.strip()) for l in open(fname, "r") if l[0] != "#"]




if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    fname = "data.txt"
    ints = read_file(fname)
    results = get_minmax(ints)

    for loc, val, type in results:
        print "%3d %4d %s" % (loc, val, type)
