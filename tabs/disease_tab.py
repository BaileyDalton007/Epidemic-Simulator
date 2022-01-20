from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton

from widgetTempletes import SliderWidget, intInputWidget

class DiseaseTab(QWidget):
    def __init__(self, parent, plotCanvas):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()

        self.plotCanvas = plotCanvas

        self.layout.addStretch(1)

        self.radSlider = SliderWidget(self, "Spread Radius")
        self.radSlider.slider.sliderInput.valueChanged.connect(lambda: self.changeRadius())
        self.layout.addLayout(self.radSlider.layout)

        self.infectionLength = intInputWidget(self, "Infection Length")
        self.layout.addLayout(self.infectionLength.layout)

        self.contSlider = SliderWidget(self, "Rate of Infection")
        self.layout.addLayout(self.contSlider.layout)
        
        self.mortSlider = SliderWidget(self, "Mortality Rate")
        self.layout.addLayout(self.mortSlider.layout)
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def changeRadius(self):
        self.plotCanvas.radius = self.radSlider.value * 0.005
        self.plotCanvas.updateGraph()
