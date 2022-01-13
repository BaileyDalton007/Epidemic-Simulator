import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

population = 50
statusList = np.zeros((population,), dtype=int)
statusList[20] = 1

np.random.seed(7)
x, y = np.random.rand(2, population)

data = np.dstack([x,y,statusList])

colormap = np.array(['b', 'r'])

def printTable():
    df = pd.DataFrame()
    df['x'] = x.tolist()
    df['y'] = x.tolist()
    df['status'] = statusList.tolist()

    print(df)

fig, ax = plt.subplots()
ax.scatter(x, y, c=colormap[statusList])
printTable()
plt.show()