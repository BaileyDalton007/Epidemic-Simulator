import sys
from plot import MplCanvas

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(1600, 800)

        sc = MplCanvas(self, width=5, height=4, dpi=200)
        sc.plot()

        #toolbar = NavigationToolbar(sc, self)
        #layout.addWidget(toolbar)

        startButton = QtWidgets.QPushButton('Start Simulation', self)

        buttonLayout = QtWidgets.QFormLayout()
        

        buttonWidget = QtWidgets.QWidget()
        buttonWidget.setLayout(buttonLayout)
        buttonLayout.addWidget(startButton)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(sc)
        layout.addWidget(buttonWidget)

        mainWidget = QtWidgets.QWidget()
        mainWidget.setLayout(layout)
        self.setCentralWidget(mainWidget)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()