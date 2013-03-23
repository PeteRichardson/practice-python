#!/usr/bin/env python

''' countbits.py - a module that counts bits two ways '''


def countbits(value):
    ''' count bits by shifting one at a time '''
    if not isinstance(value, int):
        raise TypeError("countbits requires an integer")
    bitcount = 0
    while value:
        bitcount += (value & 0x1)
        value >>= 1
    return bitcount


def countbits2(value):
    ''' count bits by shifting 4 at a time '''

    lookup_table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

    if not isinstance(value, int):
        raise TypeError("countbits2 requires an integer")
    bitcount = 0
    while value:
        bitcount += lookup_table[value & 0xF]
        value >>= 4
    return bitcount

if __name__ == '__main__':
    import unittest
    unittest.main("test_countbits")
