'''Test cases for inflectionpoints.py'''
import unittest
from ..inflectionpoints import InflectionPointFinder


class InflectionTest(unittest.TestCase):
    '''Test cases for inflectionpoints.py'''

    def test_single_max(self):
        '''test a simple single maximum in a series'''
        ipf = InflectionPointFinder((1, 2, 3, 2, 1))
        self.assertEqual(ipf.inflection_points(), ((2, 3, "Max"),))

    def test_single_min(self):
        '''test a simple single minimum in a series'''
        ipf = InflectionPointFinder((3, 2, 1, 2, 3))
        self.assertEqual(ipf.inflection_points(), ((2, 1, "Min"),))

    def test_min_max(self):
        '''test a series with both a min and a max'''
        ipf = InflectionPointFinder((3, 2, 1, 2, 3, 2, 1))
        self.assertEqual(ipf.inflection_points(),
            ((2, 1, "Min"), (4, 3, "Max")))

    def test_big_numbers(self):
        '''test a few larger numbers'''
        ipf = InflectionPointFinder((300, 2, 1000, 5000, 65, 5000, 1))
        self.assertEqual(ipf.inflection_points(),
            ((1, 2, "Min"), (3, 5000, "Max"), (4, 65, "Min"), (5, 5000, "Max")))

    def test_all_negative_numbers(self):
        '''test a series with all negative numbers'''
        ipf = InflectionPointFinder((-5, -4, -3, -4, -3, -2))
        self.assertEqual(ipf.inflection_points(),
            ((2, -3, "Max"), (3, -4, "Min")))

    def test_is_local_max(self):
        '''some spot testing for the is_local_max function'''
        self.assertTrue(InflectionPointFinder.is_local_max((1, 2, 1)))
        self.assertFalse(InflectionPointFinder.is_local_max((2, 1, 2)))
        self.assertFalse(InflectionPointFinder.is_local_max((2, 1, 1)))
        self.assertFalse(InflectionPointFinder.is_local_max((1, 1, 2)))

    def test_is_local_min(self):
        '''some spot testing for the is_local_min function'''
        self.assertTrue(InflectionPointFinder.is_local_min((2, 1, 2)))
        self.assertFalse(InflectionPointFinder.is_local_min((1, 2, 1)))
        self.assertFalse(InflectionPointFinder.is_local_min((1, 2, 2)))
        self.assertFalse(InflectionPointFinder.is_local_min((2, 2, 1)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
