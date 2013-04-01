#!/usr/bin/env python

''' countbits.py - a module that counts bits two ways '''

import unittest

def countbits(value, nbits=64, use_lookup=True):
    ''' count bits by shifting one at a time '''
    if not isinstance(value, int):
        raise TypeError("countbits requires an integer")

    if abs(value) > 1 << nbits:
        raise RuntimeError("wordsize not big enough to hold value")

    bitcount = 0

    # for negative number, limit bits to a given number
    # otherwise sign bit is extended when right shifting, and
    # the while loop will never end
    if value < 0:
        value &= (1 << nbits) - 1

    lookup_table = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
    while value:
        if use_lookup:
            bitcount += lookup_table[value & 0xF]
            value >>= 4
        else:
            bitcount += value & 0x1
            value >>= 1
    return bitcount


def selftest(verbosity=1):
    suite = unittest.TestLoader().loadTestsFromTestCase(CountbitsTests)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


class CountbitsTests(unittest.TestCase):
    ''' some countbits tests'''

    def test_simple(self):
        '''count bits in a simple number '''
        self.assertEqual(2, countbits(3))
        self.assertEqual(2, countbits(3, use_lookup=False))

    def test_zero(self):
        '''count bits in a simple number '''
        self.assertEqual(0, countbits(0))
        self.assertEqual(0, countbits(0, use_lookup=False))

    def test_None(self):
        with self.assertRaises(TypeError):
            countbits(None)
        with self.assertRaises(TypeError):
            countbits(None, use_lookup=False)

    def test_negative(self):
        self.assertEqual(64, countbits(-1))
        self.assertEqual(64, countbits(-1, use_lookup=False))

    def test_negative_with_limited_bits(self):
        self.assertEqual(4, countbits(-1, 4))
        self.assertEqual(4, countbits(-1, 4, use_lookup=False))
        self.assertEqual(5, countbits(-1, 5))
        self.assertEqual(5, countbits(-1, 5, use_lookup=False))

    def test_positive_with_limited_bits(self):
        self.assertEqual(3, countbits(7, 5))

    def test_fail_if_not_enough_bits(self):
        with self.assertRaises(RuntimeError):
            countbits(7, 2)

    def test_all(self):
        '''count bits in lots of numbers '''
        for n in range(-(2**9), 2**9):
            self.assertEqual(countbits(n), countbits(n, use_lookup=False))


if __name__ == '__main__':
    unittest.main()
