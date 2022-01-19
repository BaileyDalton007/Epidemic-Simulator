from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout

from data import DataSet
from widgetTempletes import SliderWidget, intInputWidget

class DataTab(QWidget):
    def __init__(self, parent, plotCanvas):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()

        self.plotCanvas = plotCanvas

        self.sliderWidget = SliderWidget(self, "Population")
        self.seedWidget = intInputWidget(self, "Random Seed")

        self.genButton = QPushButton("Generate Population")
        self.genButton.clicked.connect(self.generate)
        
        self.layout.addStretch(1)
        self.layout.addLayout(self.sliderWidget.layout)

        self.layout.addLayout(self.seedWidget.layout)
        self.layout.addStretch(1)

        self.layout.addWidget(self.genButton)

        self.setLayout(self.layout)

    def generate(self):
        self.plotCanvas.data = DataSet(self.seedWidget.intInput.text(), self.sliderWidget.value)
        self.plotCanvas.updateGraph()