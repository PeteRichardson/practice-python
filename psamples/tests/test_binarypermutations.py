''' Test Cases for Binary Permunations calculations '''

import unittest
import logging
from ..binarypermutations import BinaryPermutator


class Test_binarypermutations(unittest.TestCase):

    def test_empty(self):
        perm = BinaryPermutator("")
        self.assertEqual(perm.qcount, 0)
        self.assertEqual(perm.permutations(), [])

    def test_None(self):
        perm = BinaryPermutator(None)
        self.assertEqual(perm.qcount, 0)
        self.assertEqual(perm.permutations(), None)

    def test_simple(self):
        perm = BinaryPermutator("1?01")
        self.assertEqual(perm.qcount, 1)
        self.assertEqual(perm.permutations(), ['1001', '1101'])

    def test_starter(self):
        perm = BinaryPermutator("?1011")
        self.assertEqual(perm.qcount, 1)
        self.assertEqual(perm.permutations(), ['01011', '11011'])

    def test_ender(self):
        logging.debug("test_ender")
        perm = BinaryPermutator("1011?")
        self.assertEqual(perm.qcount, 1)
        self.assertEqual(perm.permutations(), ['10110', '10111'])

    def test_starter_and_ender(self):
        perm = BinaryPermutator("?1011?")
        self.assertEqual(perm.qcount, 2)
        self.assertEqual(perm.permutations(), ['010110', '010111', '110110', '110111'])

    def test_nothin_but_qs(self):
        perm = BinaryPermutator("????")
        self.assertEqual(perm.qcount, 4)
        self.assertEqual(perm.permutations(), [ '0000', '0001', '0010', '0011',
                                                '0100', '0101', '0110', '0111', 
                                                '1000', '1001', '1010', '1011', 
                                                '1100', '1101', '1110', '1111', 
                                                ])


if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    unittest.main()
