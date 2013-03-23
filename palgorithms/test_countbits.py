 #!/usr/bin/env python

''' test_countbits.py - test cases for countbits functions '''

import unittest
from countbits import countbits, countbits2


class TestCountbits(unittest.TestCase):
    ''' some countbits tests'''

    def test_simple(self):
        '''countbits - count bits in a simple number '''
        self.assertEqual(2, countbits(3))
        self.assertEqual(2, countbits2(3))

    def test_zero(self):
        '''countbits - count bits in a simple number '''
        self.assertEqual(0, countbits(0))
        self.assertEqual(0, countbits2(0))

    def test_all(self):
        '''countbits - count bits in lots of numbers '''
        for n in range(0, 2 ** 9):
            self.assertEqual(countbits(n), countbits2(n))


if __name__ == '__main__':
    unittest.main()
