#!/usr/bin/env python

''' countbits.py - a module that counts bits two ways '''

import unittest


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


def selftest(verbosity=1):
    suite = unittest.TestLoader().loadTestsFromTestCase(CountbitsTests)
    unittest.TextTestRunner(verbosity=verbosity).run(suite)


class CountbitsTests(unittest.TestCase):
    ''' some countbits tests'''

    def test_simple(self):
        '''count bits in a simple number '''
        self.assertEqual(2, countbits(3))
        self.assertEqual(2, countbits2(3))

    def test_zero(self):
        '''count bits in a simple number '''
        self.assertEqual(0, countbits(0))
        self.assertEqual(0, countbits2(0))

    def test_all(self):
        '''count bits in lots of numbers '''
        for n in range(0, 2 ** 9):
            self.assertEqual(countbits(n), countbits2(n))


if __name__ == '__main__':

    from cmd import Cmd

    class Shell(Cmd):
        def __init__(self):
            Cmd.__init__(self)
            self.prompt = "Countbits test shell> "
            self.intro = "Welcome to the Countbits test shell.\nTry 'test' or ? for other commands"

        def do_test(self, line):
            verbosity = int(line or 1)
            selftest(verbosity=verbosity)
            return False

        def do_EOF(self, line):
            return True
        do_exit = do_EOF
        do_quit = do_EOF

    Shell().cmdloop()
