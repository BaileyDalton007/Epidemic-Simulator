import matplotlib as plt
from matplotlib.pyplot import Circle

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import numpy as np
import pandas as pd

from data import DataSet

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

        self.data = DataSet(0, 0)

        self.day = 0

        self.radius = 0.0

        self.colormap = np.array(['b', 'r'])

    def plot(self):
        self.axes.scatter(self.data.x, self.data.y, c=self.colormap[self.data.statusList], picker=True);
        self.axes.xaxis.set_major_locator(plt.ticker.NullLocator())
        self.axes.set_xlim((0, 1))
        self.axes.yaxis.set_major_locator(plt.ticker.NullLocator())
        self.axes.set_ylim((0, 1))

    def drawCircles(self):
        for i in range(len(self.data.statusList)):
            if self.data.statusList[i] == 1:
                self.axes.add_patch(Circle((self.data.x[i], self.data.y[i]), self.radius, color=self.colormap[1], fill = False))


    def on_pick(self, event):
        ind = event.ind
        
        if self.data.statusList[ind].any() != 0:
            self.data.statusList[ind] = 0
            self.data.infTime[ind] = -1
        else:
            self.data.statusList[ind] = 1
            self.data.infTime[ind] = self.day

        self.updateGraph()

    def updateGraph(self):
        self.axes.cla()
        self.axes.scatter(self.data.x, self.data.y, c=self.colormap[self.data.statusList], picker=True);
        self.drawCircles()
        self.axes.xaxis.set_major_locator(plt.ticker.NullLocator())
        self.axes.set_xlim((0, 1))
        self.axes.yaxis.set_major_locator(plt.ticker.NullLocator())
        self.axes.set_ylim((0, 1))
        self.fig.canvas.mpl_connect('pick_event', self.on_pick)
        self.draw()