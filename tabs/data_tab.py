from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout

from data import DataSet

class DataTab(QWidget):
    def __init__(self, parent, plotCanvas):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()

        self.plotCanvas = plotCanvas

        self.sliderWidget = popSliderWidget(self)
        self.seedWidget = seedWidget(self)

        self.genButton = QPushButton("Generate Population")
        self.genButton.clicked.connect(self.generate)
        
        self.layout.addStretch(1)
        self.layout.addLayout(self.sliderWidget.layout)

        self.layout.addLayout(self.seedWidget.layout)
        self.layout.addStretch(1)

        self.layout.addWidget(self.genButton)

        self.setLayout(self.layout)

    def generate(self):
        self.plotCanvas.data = DataSet(self.seedWidget.seedInput.text(), self.sliderWidget.popSlider.value())
        self.plotCanvas.updateGraph()
        

class popSliderWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.slider = QWidget
        self.slider.layout = QtWidgets.QHBoxLayout()

        self.slider.popSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.slider.popSlider.setFocusPolicy(Qt.StrongFocus)
        self.slider.popSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.popSlider.setTickInterval(10)
        self.slider.popSlider.setSingleStep(1)
        self.slider.popSlider.valueChanged.connect(self.changed_slider)

        self.slider.sliderlabel = QtWidgets.QLabel("00")
        self.slider.sliderlabel.setFont(QFont("Sanserif", 10))

        self.slider.layout.addWidget(self.slider.sliderlabel)
        self.slider.layout.addWidget(self.slider.popSlider)

        # Layout of title and slider + value
        self.layout = QtWidgets.QVBoxLayout()

        self.title = QtWidgets.QLabel("Population")
        self.title.setFont(QFont("Sanserif", 12))

        self.layout.addWidget(self.title)
        self.layout.addLayout(self.slider.layout)

    def changed_slider(self):
        value = self.popSlider.value()
        if value >= 10:
            self.sliderlabel.setText(str(value))
        else:
            self.sliderlabel.setText(f'0{str(value)}')

class seedWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout()

        self.seedLabel = QtWidgets.QLabel("Random Seed")
        self.seedLabel.setFont(QFont("Sanserif", 12))

        self.seedInput = QtWidgets.QLineEdit(self)
        self.seedInput.setFixedWidth(40)
        self.seedInput.setValidator(QIntValidator())

        self.layout.addWidget(self.seedLabel)
        self.layout.addWidget(self.seedInput)
        self.layout.addStretch(1)