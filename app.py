import sys
from plot import MplCanvas
from interface import controlGUI
from simulation import Simulation

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QIcon

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Epidemic Simulator")
        self.setWindowIcon(QIcon("virus.png"))

        self.resize(1600, 800)

        self.plot = MplCanvas(self, width=5, height=4, dpi=200)
        self.plot.plot()
        
        self.simulation = Simulation(self.plot)

        controlWidget = controlGUI(self)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(self.plot)
        layout.addWidget(controlWidget)

        mainWidget = QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

        self.show()

app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()