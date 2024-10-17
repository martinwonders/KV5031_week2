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

app = QApplication(sys.argv)
window = CircleWidget()
window.show()
sys.exit(app.exec())