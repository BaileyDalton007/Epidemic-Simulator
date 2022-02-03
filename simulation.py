import numpy as np
import math

class Simulation():
    def __init__(self, plotCanvas):
        self.plotCanvas = plotCanvas
        
        # Contageousness of the virus
        self.contRate = 0.00
        # Amount of time a point will stay infected
        self.infLength = 1
        # rate of death over infection period
        self.mortRate = 0.00

    def runSimulation(self, simLength):
        radius = self.plotCanvas.radius
        for d in range(simLength):
            data = self.plotCanvas.data
        
            self.plotCanvas.day += 1
            day = self.plotCanvas.day

            self.infectedInd = np.where(data.statusList == 1)[0]
            # checks to see if patient(s) zero is selected
            if self.infectedInd.size == 0:
                return -1

            self.non_infectedInd = np.where(data.statusList == 0)[0]

            for infected in self.infectedInd:

                if (data.infTime[infected] != -1) and (day - data.infTime[infected] > self.infLength):
                    self.plotCanvas.data.statusList[infected] = 0
                    self.plotCanvas.data.infTime[infected] = -1

                else:
                    # TODO mortality rate / inflen on inf points
                    self.deathChance(infected)

                    currInfected = (data.x[infected], data.y[infected])
                    for non_infected in self.non_infectedInd:
                        currnon_Infected = (data.x[non_infected], data.y[non_infected])

                        dist = distance(currInfected, currnon_Infected)
                        if (dist <= radius):
                            self.infChance(non_infected, day)
                            
                self.plotCanvas.updateGraph()
    
    # will randomly kill points within the radius at the mortality rate
    def deathChance(self, i):
        deathChance = np.random.uniform(low=0, high=1)
        if deathChance <= (self.mortRate):
            self.plotCanvas.data.statusList[i] = 2
            self.plotCanvas.data.infTime[i] = -1

    # will randomly infect points within the radius at the infection rate
    def infChance(self, i, day):
        infChance = np.random.uniform(low=0, high=1)
        if (infChance <= self.contRate):
            self.plotCanvas.data.statusList[i] = 1
            self.plotCanvas.data.infTime[i] = day


def distance(p1, p2):
    distance = math.sqrt( ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) )
    return distance
                


