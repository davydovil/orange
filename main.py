import sys
from random import randrange

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        a = randrange(10, 160, 2)
        self.x = randrange(a, 545 - a, 2)
        self.y = randrange(a, 431 - a, 2)
        qp.setBrush(QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255)))
        qp.drawEllipse(self.x, self.y, a, a)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())