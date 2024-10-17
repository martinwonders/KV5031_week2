import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt

class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw Circle")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawEllipse(50,50,200,200)

class ShapeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Draw Shapes")

    def paintEvent(self, event):
        painter = QPainter(self)
        #draw a rectangle
        painter.drawRect(50,50,150,100)
        painter.setRenderHint(QPainter.Antialiasing)
        #draw a line
        painter.drawLine(50, 200, 200, 250)


app = QApplication(sys.argv)
window = ShapeWidget()
window.show()
sys.exit(app.exec())