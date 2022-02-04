from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtGui import QFont, QIntValidator
from simulation import Simulation
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

        self.csvButton = QPushButton("Save Current Simulation as CSV")
        self.csvButton.clicked.connect(self.saveSim)
        self.layout.addWidget(self.csvButton)

        self.setLayout(self.layout)

    def startSim(self):
        if self.simLength.intInput.text() == "":
            self.notiflabel.setText("Please Specify Length of Simulation")
        else:
            self.notiflabel.setText("")
            
            simLength = int(self.simLength.intInput.text())
            if self.simulation.runSimulation(simLength) == -1:
                self.notiflabel.setText("Please Click a Point to Start Infection")
            else:
                self.notiflabel.setText("")

    def saveSim(self):
        self.simulation.saveSim()
