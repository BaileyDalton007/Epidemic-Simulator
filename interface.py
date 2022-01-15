from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QTabWidget

class controlGUI(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.dataTab = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.dataTab,"Data")
        self.tabs.addTab(self.tab2,"Tab 2")
        
        # Create first tab
        self.dataTab.layout = QtWidgets.QVBoxLayout(self)
        self.pushButton1 = QPushButton("Generate Population")
        self.dataTab.layout.addWidget(self.pushButton1)
        self.dataTab.setLayout(self.dataTab.layout)
        
        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)