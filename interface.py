from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton, QTabWidget, QGridLayout

from data import DataSet
class controlGUI(QWidget):
    def __init__(self, parent, plotCanvas):
        super(QWidget, self).__init__(parent)
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        
        self.plotCanvas = plotCanvas

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.dataTab = QWidget()
        self.tab2 = QWidget()
        
        # Add tabs
        self.tabs.addTab(self.dataTab,"Data")
        self.tabs.addTab(self.tab2,"Tab 2")
        
        # Create first tab
        self.dataTab.layout = QGridLayout(self)

        self.sliderWidget = popSliderWidget(self)
        self.seedWidget = seedWidget(self)

        self.genButton = QPushButton("Generate Population")
        self.genButton.clicked.connect(self.generate)

        self.dataTab.layout.addLayout(self.sliderWidget.layout, 0, 0)

        self.dataTab.layout.addLayout(self.seedWidget.layout, 1, 0)

        self.dataTab.layout.addWidget(self.genButton)

        self.dataTab.setLayout(self.dataTab.layout)
        
        # Add tabs to widget
        self.mainLayout.addWidget(self.tabs)
        self.setLayout(self.mainLayout)

    def generate(self):
        self.plotCanvas.data = DataSet(self.seedWidget.seedInput.text(), self.sliderWidget.popSlider.value())
        self.plotCanvas.updateGraph()


class popSliderWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout()

        self.popSlider = QtWidgets.QSlider(Qt.Horizontal)
        self.popSlider.setFocusPolicy(Qt.StrongFocus)
        self.popSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.popSlider.setTickInterval(10)
        self.popSlider.setSingleStep(1)
        self.popSlider.valueChanged.connect(self.changed_slider)

        self.sliderlabel = QtWidgets.QLabel("00")
        self.sliderlabel.setFont(QFont("Sanserif", 10))

        self.layout.addWidget(self.sliderlabel)
        self.layout.addWidget(self.popSlider)


    def changed_slider(self):
        value = self.popSlider.value()
        if value >= 10:
            self.sliderlabel.setText(str(value))
        else:
            self.sliderlabel.setText(f'0{str(value)}')

class seedWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QGridLayout()

        self.seedLabel = QtWidgets.QLabel("Random Seed")
        self.seedLabel.setFont(QFont("Sanserif", 12))

        self.seedInput = QtWidgets.QLineEdit(self)
        self.seedInput.setFixedWidth(40)
        self.seedInput.setValidator(QIntValidator())

        self.layout.addWidget(self.seedLabel, 0, 0)
        self.layout.addWidget(self.seedInput, 0, 1)
        self.layout.setAlignment(self.seedInput, Qt.AlignLeft)
        self.layout.setHorizontalSpacing(0)
