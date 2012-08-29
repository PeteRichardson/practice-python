#!/usr/bin/env python

''' countbits.py - a script to test bit manipulation
                    in python'''

import unittest


def countbits(hex):
    sum = 0
    remainder = hex
    while remainder > 0:
        sum = sum + (remainder & 0x1)
        remainder = remainder >> 1
    return sum

lookuptable = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]


def countbits2(hex):
    sum = 0
    remainder = hex
    while remainder > 0:
        byte = remainder & 0xF
        sum = sum + lookuptable[byte]
        remainder = remainder >> 4
    return sum


class TestCountBits(unittest.TestCase):

    def test_ints(self):
        for i in range(0, 2 ** 20):
            self.assertEqual(countbits(i), countbits(i))

if __name__ == "__main__":
    unittest.main()
    #print countbits(0xd)
