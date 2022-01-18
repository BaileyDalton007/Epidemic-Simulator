from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QTabWidget, QGridLayout

from tabs.data_tab import DataTab
class controlGUI(QWidget):
    def __init__(self, parent, plotCanvas):
        super(QWidget, self).__init__(parent)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.dataTab = DataTab(self, plotCanvas)
        self.tab2 = QWidget()
        
        # Add tabs
        self.tabs.addTab(self.dataTab,"Data")
        self.tabs.addTab(self.tab2,"Tab 2")

        # Add tabs to widget
        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)