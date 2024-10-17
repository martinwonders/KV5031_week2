import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QBrush, QColor, QPen


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

class CustomShapeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Shapes")

    def paintEvent(self, event):
        painter = QPainter(self)

        #setup a brush colour
        brush = QBrush(QColor(100,100,255))
        painter.setBrush(brush)

        #setup a pen with colour and thickness
        pen = QPen(QColor(0,0,0))
        pen.setWidth(5)
        painter.setPen(pen)

        #Draw a filled rectangle
        painter.drawRect(50,50,150,100)

        #Draw a circle
        painter.drawEllipse(250, 50, 100,100)



app = QApplication(sys.argv)
window = CustomShapeWidget()
window.show()
sys.exit(app.exec())