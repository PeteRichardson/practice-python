#!/usr/bin/env python

''' firstsim.py - my first simpy simulator '''


import SimPy.Simulation
import random
import time

class G:    # Global variables
    Rnd = random.Random(time.time())


class Machine(SimPy.Simulation.Process):
    '''A machine that breaks and is fixed'''
    UpRate = 1 / 1.0
    RepairRate = 1 / 0.5
    TotalUptime = 0.0
    NextID = 0

    def __init__(self):
        SimPy.Simulation.Process.__init__(self)
        self.startuptime = 0.0
        self.id = Machine.NextID
        Machine.NextID += 1

    def run(self):
        ''' Do some work '''
        while 1:
            self.startuptime = SimPy.Simulation.now()
            uptime = G.Rnd.expovariate(Machine.UpRate)
            yield SimPy.Simulation.hold, self, uptime

            Machine.TotalUptime += SimPy.Simulation.now() - self.startuptime
            repairtime = G.Rnd.expovariate(Machine.RepairRate)
            yield SimPy.Simulation.hold, self, repairtime


def main():
    '''Start the whole simulation'''
    SimPy.Simulation.initialize()
    for i in range(2):
        machine = Machine()
        SimPy.Simulation.activate(machine, machine.run())

    maxsimtime = 1000.0
    SimPy.Simulation.simulate(until=maxsimtime)
    print "the percentage of uptime was {}".format(
        Machine.TotalUptime / (2 * maxsimtime))


if __name__ == "__main__":
    main()
