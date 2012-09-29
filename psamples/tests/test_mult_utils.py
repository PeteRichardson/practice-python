#!/usr/bin/env python

''' test_allmult.py - unittests for allmult.py '''

import unittest
from ..mult_utils import all_mult, mult_half


class Test_Allmult(unittest.TestCase):

    def test_empty(self):
        '''test empty input'''
        self.assertEqual(all_mult([]), [])

    def test_single(self):
        ''' test single element array '''
        self.assertEqual(all_mult([1]), [1])

    def test_simple(self):
        '''simple test case'''
        self.assertEqual(all_mult([1, 2, 3]), [6, 3, 2])

    def test_half_simple(self):
        ''' test the half function '''
        self.assertEqual(mult_half([3, 4, 5]), [3, 12, 60])


if __name__ == "__main__":
    unittest.main()