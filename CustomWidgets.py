import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import (QPainter, QBrush, QColor, QPen)
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


class MultipleShapesWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Multiple Shapes")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        #set the pen and brush for the first shape
        pen = QPen(Qt.DashLine)
        pen.setWidth(2)
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.setPen(pen)

        #Draw a rectangle
        painter.drawRect(50,50,100,100)

        #Change the pen and brush
        pen.setStyle(Qt.DotLine)
        brush.setColor(Qt.yellow)
        painter.setBrush(brush)
        painter.setPen(pen)

        painter.drawEllipse(200, 50, 100,100)

        #Draw a line with a thicker pen
        pen.setWidth(5)
        painter.setPen(pen)
        painter.drawLine(50, 200, 300, 200)



app = QApplication(sys.argv)
window = MultipleShapesWidget()
window.show()
sys.exit(app.exec())