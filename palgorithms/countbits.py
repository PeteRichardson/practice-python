#!/usr/bin/env python

''' countbits.py - a module that counts bits two ways '''


def countbits(value):
    ''' count bits by shifting one at a time '''
    if value == None:
        raise RuntimeError("Expected Integer, Got None")
    bitcount = 0
    while value > 0:
        bitcount = bitcount + (value & 0x1)
        value = value >> 1
    return bitcount

lookup_table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]


def countbits2(value):
    ''' count bits by shifting 4 at a time '''
    if value == None:
        raise RuntimeError("Expected Integer, Got None")
    bitcount = 0
    while value > 0:
        bitcount = bitcount + lookup_table[value & 0xF]
        value = value >> 4
    return bitcount

if __name__ == '__main__':
    import unittest
    unittest.main("test_countbits")
