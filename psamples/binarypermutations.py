''' some repl testing '''

from pprint import pprint, pformat
import logging


logger = logging.getLogger(__name__)


class BinaryPermutator:
    '''Class to return all permutations of binary numbers with
        question marks replaced by a binary iteration of digits'''

    def __init__(self, data):
        self.data = data
        if data == None:
            self.statics = None
            self.qcount = 0
        else:
            self.statics = data.split("?")
            self.qcount = 0 if (data == None or data == "") else len(self.statics) - 1

    def permutations(self):
        if self.data == None:
            return None
        if self.data == "":
            return []

        result = []
        for perm in range(2 ** self.qcount):
            permstr = "{0:0{width}b} ".format(perm, width=self.qcount)
            res = ''.join(["%s%s" % pair for pair in zip(self.statics, permstr)]).strip()
            result.append(res)
        return result


if __name__ == "__main__":
    import unittest
    unittest.main("test_binarypermutations")
