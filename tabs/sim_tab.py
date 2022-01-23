from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton

from widgetTempletes import SliderWidget, intInputWidget


class SimulationTab(QWidget):
    def __init__(self, parent, simulation):
        super(QWidget, self).__init__(parent)

        self.simulation = simulation

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addStretch(1)

        self.simLength = intInputWidget(self, "Days Of Simulation")
        self.layout.addLayout(self.simLength.layout)
        
        self.layout.addStretch(1)
        
        self.startButton = QPushButton("Start Simulation")
        self.startButton.clicked.connect(self.startSim)
        self.layout.addWidget(self.startButton)
        self.setLayout(self.layout)

    def startSim(self):
        self.simulation.runSimulation(int(self.simLength.intInput.text()))
