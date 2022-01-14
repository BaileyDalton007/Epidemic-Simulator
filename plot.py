from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np
import pandas as pd

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        np.random.seed(7)

        self.population = 50
        self.x, self.y = np.random.rand(2, self.population)
        self.statusList = np.zeros((self.population,), dtype=int)
        self.colormap = np.array(['b', 'r'])

    def plot(self):
        self.axes.scatter(self.x, self.y, c=self.colormap[self.statusList], picker=True);
    
    def printTable(self):
        df = pd.DataFrame()
        df['x'] = self.x.tolist()
        df['y'] = self.y.tolist()
        df['status'] = self.statusList.tolist()
        print(df)

    def on_pick(self, event):
        ind = event.ind
        
        if self.statusList[ind].any() != 0:
            self.statusList[ind] = 0
        else:
            self.statusList[ind] = 1
        self.updateGraph()

    def updateGraph(self):
        self.axes.cla()
        self.axes.scatter(self.x, self.y, c=self.colormap[self.statusList], picker=True);
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.draw()