#!/usr/bin/env python

class InflectionPoints:
    def __init__(self, values):
        self.values = values

    def __str__(self):
        return ",".join([str(v) for v in self.values])
    
    def points(self):
        for i in range(1, len(self.values)-1):
            yield( (i, (self.values[i-1], self.values[i], self.values[i+1])) )
            
    @classmethod
    def isLocalMax(cls, t):
        return (t[0] < t[1] and t[1] > t[2])
        
    @classmethod
    def isLocalMin(cls, t):
        return (t[0] > t[1] and t[1] < t[2])
        
    @classmethod
    def isInflectionPoint(cls, t):
        return (cls.isLocalMax(t) or cls.isLocalMin(t))
    
    def inflectionPoints(self):
        results = []
        for p in self.points():
            i = p[0]
            t = p[1]
            if self.isLocalMax(t):
                results.append((i,t[1],"Max"))
            elif (self.isLocalMin(t)):
                results.append((i,t[1], "Min"))
        return tuple(results)

if __name__ == '__main__':
    data = [(1,2,3,2,1),
            (3,2,1,2,3,2,1),
            (300,2,1000,5000,65,5000,1),
            (-5,-4,-3,-4,-3,-2)]
    
    for points in data:
            ips = InflectionPoints(points)
            print "------------------"
            print points
            for p in ips.inflectionPoints():
                print p
            
