#!/usr/bin/env python
'''inflectionpoints.py - Calculate local mins and maxes of a series of ints'''


class InflectionPointFinder:
    '''Calculate local mins and maxes of a series of ints'''
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return ",".join([str(v) for v in self.values])

    def points(self):
        '''Generate all the points in the series'''
        for index in range(1, len(self.values) - 1):
            yield((index,  (self.values[index - 1],
                            self.values[index],
                            self.values[index + 1])))

    @classmethod
    def is_local_max(cls, tup):
        '''True if the center item of tuple is a local max'''
        return (tup[0] < tup[1] and tup[1] > tup[2])

    @classmethod
    def is_local_min(cls, tup):
        '''True if the center item of tuple is a local min'''
        return (tup[0] > tup[1] and tup[1] < tup[2])

    @classmethod
    def is_inflection_point(cls, tup):
        '''True if the center item of tuple is an inflection point'''
        return (cls.is_local_max(tup) or cls.is_local_min(tup))

    def inflection_points(self):
        '''Return list of all inflection points
        Maybe should be changed to a generator?'''
        results = []
        for pnt in self.points():
            index = pnt[0]
            tup = pnt[1]
            if self.is_local_max(tup):
                results.append((index, tup[1], "Max"))
            elif (self.is_local_min(tup)):
                results.append((index, tup[1], "Min"))
        return tuple(results)

if __name__ == '__main__':
    TEST_DATA = [(1, 2, 3, 2, 1),
            (3, 2, 1, 2, 3, 2, 1),
            (300, 2, 1000, 5000, 65, 5000, 1),
            (-5, -4, -3, -4, -3, -2)]

    for points in TEST_DATA:
        ipf = InflectionPointFinder(points)
        print "------------------"
        print points
        for point in ipf.inflection_points():
            print point
