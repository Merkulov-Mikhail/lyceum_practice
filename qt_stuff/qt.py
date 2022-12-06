import sys
from random import randint
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor

from untitled import *


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.mk)

    def mk(self):
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        r = randint(10, 100)
        qp.setBrush(QColor(f"#{hex(randint(0, 255))[2:]}{hex(randint(0, 255))[2:]}{hex(randint(0, 255))[2:]}"))
        x, y = randint(50, 250), randint(50, 250)
        qp.drawEllipse(x, y, x + r, y + r)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    m = Main()
    m.show()
    app.exec()
