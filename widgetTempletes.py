from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QIntValidator
from PyQt5.QtWidgets import QWidget, QPushButton


class SliderWidget(QWidget):
    def __init__(self, parent, title):
        super(QWidget, self).__init__(parent)
        self.slider = QWidget()
        self.slider.layout = QtWidgets.QHBoxLayout()

        self.value = 0

        self.slider.sliderInput = QtWidgets.QSlider(Qt.Horizontal)
        self.slider.sliderInput.setFocusPolicy(Qt.StrongFocus)
        self.slider.sliderInput.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.slider.sliderInput.setTickInterval(10)
        self.slider.sliderInput.setSingleStep(1)

        self.slider.sliderInput.valueChanged.connect(self.changed_slider)

        self.slider.sliderlabel = QtWidgets.QLabel("00")
        self.slider.sliderlabel.setFont(QFont("Sanserif", 10))

        self.slider.layout.addWidget(self.slider.sliderlabel)
        self.slider.layout.addWidget(self.slider.sliderInput)

        # Layout of title and slider + value
        self.layout = QtWidgets.QVBoxLayout()

        self.title = QtWidgets.QLabel(title)
        self.title.setFont(QFont("Sanserif", 12))

        self.layout.addWidget(self.title)
        self.layout.addLayout(self.slider.layout)

    def changed_slider(self):
        self.value = self.slider.sliderInput.value()
        if self.value >= 10:
            self.slider.sliderlabel.setText(str(self.value))
        else:
            self.slider.sliderlabel.setText(f'0{str(self.value)}')

class intInputWidget(QWidget):
    def __init__(self, parent, title):
        super(QWidget, self).__init__(parent)
        self.layout = QtWidgets.QHBoxLayout()

        self.intLabel = QtWidgets.QLabel(title)
        self.intLabel.setFont(QFont("Sanserif", 12))

        self.intInput = QtWidgets.QLineEdit(self)
        self.intInput.setFixedWidth(40)
        self.intInput.setValidator(QIntValidator())

        self.layout.addWidget(self.intLabel)
        self.layout.addWidget(self.intInput)
        self.layout.addStretch(1)
