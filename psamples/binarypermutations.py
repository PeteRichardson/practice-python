'''BinaryPermutator - return all permutations of binary numbers with
   question marks replaced by a binary iteration of digits'''

import logging


logger = logging.getLogger(__name__)


class BinaryPermutator:
    '''Class to return all permutations of binary numbers with
        question marks replaced by a binary iteration of digits'''

    def __init__(self, data):
        if data:
            self.statics = data.split("?")
            self.qcount = 0 if (data is None or data == "") else len(self.statics) - 1
        else:
            self.statics = None
            self.qcount = 0

    def permutations(self):
        if self.qcount == 0:
            yield self.statics
        else:
            for perm in range(2 ** self.qcount):
                permstr = "{0:0{width}b} ".format(perm, width=self.qcount)
                res = ''.join(["%s%s" % pair for pair in zip(self.statics, permstr)]).strip()
                yield res


if __name__ == "__main__":
    import unittest

    class Test_BinaryPermutator(unittest.TestCase):
        def test_empty(self):
            perm = BinaryPermutator("")
            self.assertEqual(perm.qcount, 0)
            self.assertEqual(list(perm.permutations()), [None])

        def test_None(self):
            perm = BinaryPermutator(None)
            self.assertEqual(perm.qcount, 0)
            self.assertEqual(list(perm.permutations()), [None])

        def test_simple(self):
            perm = BinaryPermutator("1?01")
            self.assertEqual(perm.qcount, 1)
            self.assertEqual(list(perm.permutations()), ['1001', '1101'])

        def test_starter(self):
            perm = BinaryPermutator("?1011")
            self.assertEqual(perm.qcount, 1)
            self.assertEqual(list(perm.permutations()), ['01011', '11011'])

        def test_ender(self):
            logging.debug("test_ender")
            perm = BinaryPermutator("1011?")
            self.assertEqual(perm.qcount, 1)
            self.assertEqual(list(perm.permutations()), ['10110', '10111'])

        def test_starter_and_ender(self):
            perm = BinaryPermutator("?1011?")
            self.assertEqual(perm.qcount, 2)
            self.assertEqual(list(perm.permutations()), ['010110', '010111', '110110', '110111'])

        def test_nothin_but_qs(self):
            perm = BinaryPermutator("????")
            self.assertEqual(perm.qcount, 4)
            self.assertEqual(list(perm.permutations()), [ '0000', '0001', '0010', '0011',
                                                    '0100', '0101', '0110', '0111', 
                                                    '1000', '1001', '1010', '1011', 
                                                    '1100', '1101', '1110', '1111', 
                                                    ])

    unittest.main()
