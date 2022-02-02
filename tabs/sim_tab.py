from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QFont, QIntValidator
from widgetTempletes import SliderWidget, intInputWidget


class SimulationTab(QWidget):
    def __init__(self, parent, simulation):
        super(QWidget, self).__init__(parent)

        self.simulation = simulation

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addStretch(1)

        self.simLength = intInputWidget(self, "Days Of Simulation")
        self.layout.addLayout(self.simLength.layout)
        
        # label to give errors if trying to run a simlulation
        self.notiflabel = QtWidgets.QLabel("")
        self.notiflabel.setFont(QFont("Sanserif", 10))

        self.layout.addWidget(self.notiflabel)

        self.layout.addStretch(1)
        
        self.startButton = QPushButton("Start Simulation")
        self.startButton.clicked.connect(self.startSim)
        self.layout.addWidget(self.startButton)
        self.setLayout(self.layout)

    def startSim(self):
        if self.simulation.runSimulation(int(self.simLength.intInput.text())) == -1:
            self.notiflabel.setText("Please Click a Point to Start Infection")
        else:
            self.notiflabel.setText("")
