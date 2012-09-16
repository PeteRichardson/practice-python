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
        logger.debug("self.qcount = %d", self.qcount)
        logger.debug("self.statics = %s" % pformat(self.statics))
        for perm in range(2 ** self.qcount):
            logger.debug("perm = %s", perm)
            permstr = "{0:0{width}b} ".format(perm, width=self.qcount)
            logger.debug("permstr = %s" % permstr)
            z = zip(self.statics, permstr)
            logger.debug("z = %s" % pformat(z))
            res = ''.join(["%s%s" % pair for pair in z]).strip()
            logger.debug("res = %s" % res)
            result.append(res)
        return result


if __name__ == "__main__":
    import unittest
    unittest.main("test_binarypermutations")
