import sys
from main import MplCanvas

import matplotlib
matplotlib.use('Qt5Agg')

from PyQt5 import QtWidgets

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        sc = MplCanvas(self, width=5, height=5, dpi=100)
        sc.plot()

        toolbar = NavigationToolbar(sc, self)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()