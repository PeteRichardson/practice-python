''' test_storecredit.py - unit tests for google code jam problem: Store Credit '''

import unittest
from storecredit import Store


class Test_StoreCredit(unittest.TestCase):

    def test_inputsplit(self):
        inp = '''3
                100
                3
                5 75 25
                200
                7
                150 24 79 50 88 345 3
                8
                8
                2 1 9 4 4 56 90 3'''

        store = Store(inp)
        self.assertEqual(store.N, 3)
        self.assertEqual(len(store.cases), 3)
        self.assertEqual(store.cases[0].C, 100)
        self.assertEqual(store.cases[0].I, 3)
        self.assertEqual(len(store.cases[0].P), 3)
        self.assertEqual(store.cases[0].P, [5, 75, 25])
        self.assertEqual(store.cases[0].solution, [2, 3])

        self.assertEqual(store.cases[1].C, 200)
        self.assertEqual(store.cases[1].I, 7)
        self.assertEqual(len(store.cases[1].P), 7)
        self.assertEqual(store.cases[1].P, [150, 24, 79, 50, 88, 345, 3])
        self.assertEqual(store.cases[1].solution, [1, 4])

        self.assertEqual(store.cases[2].C, 8)
        self.assertEqual(store.cases[2].I, 8)
        self.assertEqual(len(store.cases[2].P), 8)
        self.assertEqual(store.cases[2].P, [2, 1, 9, 4, 4, 56, 90, 3])
        self.assertEqual(store.cases[2].solution, [4, 5])


if __name__ == '__main__':
    unittest.main()
