''' storecredit.py - code for google code jam Store Credit problem '''

class Case:
    def __init__(self, threelines):
        #pdb.set_trace()
        self.C = int(threelines[0])
        self.I = int(threelines[1])
        self.P = [int(x) for x in (threelines[2]).split()]
        self.solution = None

    def solve(self):
        ''' find pair of items whose prices add up to C '''
        needs = {}
        for i in range(len(self.P)):
            price = self.P[i]
            #print "price =", price, 
            if price in needs:
                self.solution = [needs[price], i + 1]
                #print "Found a solution!", self.solution
                return
            else:
                #print "adding %d => %d" % (self.C - price, i)
                needs[self.C - price] = i + 1


class Store:
    def __init__(self, inp):
        self.lines = inp.split("\n")
        self.N = int(self.lines[0])
        self.cases = []

        for c in range(self.N):
            case = Case(self.lines[(c * 3) + 1:(c * 3) + 4])
            case.solve()
            self.cases.append(case)

