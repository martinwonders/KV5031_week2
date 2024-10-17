import sys
from PySide6.QtGui import QPainter, QBrush, QColor
from PySide6.QtWidgets import QWidget, QApplication


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

app = QApplication(sys.argv)
window = MouseEventWidget()
window.show()
sys.exit(app.exec())