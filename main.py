import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
import numpy as np
import pandas as pd

population = 50
np.random.seed(7)
x, y = np.random.rand(2, population)

statusList = np.zeros((population,), dtype=int)

colormap = np.array(['b', 'r'])

def printTable():
    df = pd.DataFrame()
    df['x'] = x.tolist()
    df['y'] = x.tolist()
    df['status'] = statusList.tolist()

    print(df)

def on_pick(event):
    ind = event.ind

    if statusList[ind].any() != 0:
        statusList[ind] = 0
    else:
        statusList[ind] = 1
    
    plt.clf()
    plt.scatter(x, y, c=colormap[statusList], picker=True);
    plt.draw()

fig, ax = plt.subplots()
ax.scatter(x, y, c=colormap[statusList], picker=True)
fig.canvas.mpl_connect('pick_event', on_pick)

plt.show()
plt.draw()