''' bsort.py - a module to sort arrays using bubblesort '''
#!/usr/bin/env python

import logging

logger = logging.getLogger(__name__)


def bubblesort(array):
    ''' repeatedly walk the array swapping items that are
        out of order until no swaps are possible '''

    if array == None:
        return array

    array_copy = list(array)
    if (len(array_copy) <= 1):
        return array_copy

    item_swapped = True
    while (item_swapped == True):
        item_swapped = False
        for n in range(0, len(array_copy) - 1):
            if array_copy[n] > array_copy[n + 1]:
                item_swapped = True
                logger.debug("swapping %d [%s] with %d [%s]" %
                    (n, str(array_copy[n]), n + 1, str(array_copy[n + 1])))
                array_copy[n], array_copy[n + 1] = array_copy[n + 1], array_copy[n]
    return array_copy

if __name__ == "__main__":
    import unittest
    unittest.main("test_bsort")
