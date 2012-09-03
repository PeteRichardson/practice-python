#!/usr/bin/env python

''' countbits.py - a script to test bit manipulation
                    in python'''

import unittest


def countbits(hex_val):
    ''' countbits '''
    bit_count = 0
    remainder = hex_val
    while remainder > 0:
        bit_count = bit_count + (remainder & 0x1)
        remainder = remainder >> 1
    return bit_count

lookuptable = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]


def countbits2(hex_val):
    ''' countbits2 '''
    bit_count = 0
    remainder = hex_val
    while remainder > 0:
        byte = remainder & 0xF
        bit_count = bit_count + lookuptable[byte]
        remainder = remainder >> 4
    return bit_count


class TestCountBits(unittest.TestCase):
    ''' testcases '''

    def test_ints(self):
        ''' test_ints '''
        for i in range(0, 2 ** 10):
            self.assertEqual(countbits(i), countbits(i))

    def test_2(self):
        ''' test 2 '''
        self.assertEqual(countbits(2), 1)

if __name__ == "__main__":
    unittest.main()
    #print countbits(0xd)
