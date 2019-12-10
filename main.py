import sys
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication, QWidget


class Widget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.btn.clicked.connect(self.run)

        self.flag = False

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, mod):
        qp = mod
        pen = QPen(QColor(255, 255, 0), 5)
        qp.setPen(pen)
        hw = randint(10, 100)
        qp.drawEllipse(150 - hw // 2, 200 - hw // 2, hw, hw)

    def run(self):
        self.flag = True
        self.update()


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())