import numpy as np
import pandas as pd
from csvGenerator import writeCSV

class DataSet:
    def __init__(self, seed, pop):
        # If no seed input, seed of 0 is assumed
        if seed == "" or seed == None:
            np.random.seed(0)
        else:
            np.random.seed(int(seed))

        self.population = pop
        self.x, self.y = np.random.rand(2, self.population)
        self.statusList = np.zeros((self.population), dtype=int)
        self.infTime = np.full((self.population), -1)

        # nested arrays to save each day's status and infTime to csv
        self.statusHistory = np.zeros((self.population, 1), dtype=int)
        self.infHistory = -1* np.ones((self.population, 1), dtype=int)

    def printTable(self):
        df = pd.DataFrame()
        df['x'] = self.x.tolist()
        df['y'] = self.y.tolist()
        df['status'] = self.statusList.tolist()
        df['infTime'] = self.infTime.tolist()

        print(df)

    def saveData(self):
        df = pd.DataFrame()
        df['x'] = self.x.tolist()
        df['y'] = self.y.tolist()
        df['status'] = self.statusHistory.tolist()
        df['infTime'] = self.infHistory.tolist()

        writeCSV(df)

    def updateHistory(self):
        currStatus = [[item] for item in self.statusList]
        self.statusHistory = np.hstack((self.statusHistory, currStatus))

        currTime = [[item] for item in self.infTime]
        self.infHistory = np.hstack((self.infHistory, currTime))

    # updates history when the user selects point on plot
    def plotHistory(self):
        self.statusHistory = np.delete(self.statusHistory, -1, 1)
        self.infHistory = np.delete(self.infHistory, -1, 1)

        self.updateHistory()
