import numpy as np
import pandas as pd

class DataSet:
    def __init__(self, seed, pop):
        # If no seed input, seed of 0 is assumed
        if seed == "" or seed == None:
            np.random.seed(0)
        else:
            np.random.seed(int(seed))

        self.population = pop
        self.x, self.y = np.random.rand(2, self.population)
        self.statusList = np.zeros((self.population,), dtype=int)

    def printTable(self):
        df = pd.DataFrame()
        df['x'] = self.x.tolist()
        df['y'] = self.y.tolist()
        df['status'] = self.statusList.tolist()
        print(df)
