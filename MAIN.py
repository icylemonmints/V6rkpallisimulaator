# See on projekti põhifail. See kood käivitab hetkel tühja akna.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Võrkpallirotatsioonid")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())