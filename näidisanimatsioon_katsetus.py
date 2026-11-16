import sys

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve

from MAIN import MainWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(600, 600)
        self.child = QWidget(self)
        self.child.setStyleSheet("background-color:red;border-radius:15px;")
        self.child.resize(100, 100)
        #kasutatav osa
        #tee animation property, give start and end and duration
        self.anim = QPropertyAnimation(self.child, b"pos")
        self.anim.setEndValue(QPoint(400, 400))
        self.anim.setDuration(1500)
        self.anim.start()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())