import numpy as np
import math

class Simulation():
    def __init__(self, plotCanvas):
        self.plotCanvas = plotCanvas
        
        # Contageousness of the virus
        self.contRate = 0.00
        # Amount of time a point will stay infected
        self.infLength = 1

        # Keep track of day counts between runSim method calls
        self.currDay = 0
        # TODO check to make sure patient 0 is selected

    def runSimulation(self, simLength):
        radius = self.plotCanvas.radius

        for d in range(simLength):
            # day count is 1 based
            day = d + self.currDay
            data = self.plotCanvas.data

            infectedInd = np.where(data.statusList == 1)[0]
            non_infectedInd = np.where(data.statusList != 1)[0]
            
            for infected in infectedInd:
                if (day - data.infTime[infected]) > self.infLength:
                    self.plotCanvas.data.statusList[infected] = 0
                else:
                    currInfected = (data.x[infected], data.y[infected])
                    for non_infected in non_infectedInd:
                        currnon_Infected = (data.x[non_infected], data.y[non_infected])

                        dist = distance(currInfected, currnon_Infected)
                        if (dist <= radius):

                            # will randomly infect points within the radius at the infection rate
                            chance = np.random.uniform(low=0, high=1)
                            if (chance <= self.contRate):
                                self.plotCanvas.data.statusList[non_infected] = 1
                                self.plotCanvas.data.infTime[non_infected] = day
                self.plotCanvas.updateGraph()
        self.currDay += simLength

def distance(p1, p2):
    distance = math.sqrt( ((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2) )
    return distance
                


