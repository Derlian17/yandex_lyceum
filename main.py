from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QWidget
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPen, QPainter, QColor
from random import randint
import sys

app = QApplication(sys.argv)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(0, 0, 300, 300)
        self.label = QLabel(self)
        self.button = QPushButton(self)
        self.button.clicked.connect(self.run)
        self.radius = []

    def paintEvent(self, event):
        pen = QPen(QColor('yellow'), 5)
        qd = QPainter()
        qd.begin(self)
        qd.setPen(pen)
        for i in self.radius:
            qd.drawEllipse(QPoint(150, 150), i, i)
        qd.end()

    def run(self):
        self.radius.append(randint(50, 150))
        self.repaint()


ex = MainWindow()
ex.show()
sys.excepthook = except_hook
sys.exit(app.exec())