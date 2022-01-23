from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QTabWidget, QGridLayout

from tabs.data_tab import DataTab
from tabs.disease_tab import DiseaseTab
from tabs.sim_tab import SimulationTab
class controlGUI(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.dataTab = DataTab(self, parent.plot)
        self.diseaseTab = DiseaseTab(self, parent.plot, parent.simulation)
        self.simTab = SimulationTab(self, parent.simulation)

        
        # Add tabs
        self.tabs.addTab(self.dataTab,"Data")
        self.tabs.addTab(self.diseaseTab,"Disease")
        self.tabs.addTab(self.simTab,"Simulation")

        # Add tabs to widget
        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)