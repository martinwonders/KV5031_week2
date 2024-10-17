import sys
from PySide6.QtGui import QPainter, QBrush, QColor, QPen
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Qt, QRect

class MouseEventWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Events")
        self.click_position = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.click_position:
            painter.setBrush(QBrush(QColor(250,100,100)))
            painter.drawEllipse(self.click_position, 50,50)

    def mousePressEvent(self, event):
        # Store the click position and trigger a redraw
        self.click_position = event.position()
        self.update()


class DragShapeWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Drag Events")
        self.start_position = None
        self.end_position = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if self.start_position and self.end_position:
            #Draw a rectangle based on mouse drag
            rect = QRect(self.start_position, self.end_position)
            painter.setPen(QPen(Qt.black, 2))
            painter.setBrush(QBrush(QColor(150,200,255, 150)))
            painter.drawRect(rect)
            painter.end()

    def mousePressEvent(self, event):
        #Record starting position
        self.start_position = event.position().toPoint()

    def mouseMoveEvent(self, event):
        #update end position during drag
        self.end_position = event.position().toPoint()
        self.update()

    def mouseReleaseEvent(self, event):
        #Finalise rectangle on mouse event
        self.end_position = event.position().toPoint()
        self.update()


app = QApplication(sys.argv)
window = DragShapeWidget()
window.show()
sys.exit(app.exec())