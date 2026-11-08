import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QGraphicsLineItem
)
from PySide6.QtGui import QBrush, QPen, QColor
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Võrkpallirotatsioonide simulaator")

        S = 50
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 10*S, 10*S)

        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        plats = QGraphicsRectItem(0.5*S, 0.5*S, 9*S, 9*S)
        plats.setBrush(QBrush(QColor("#cb784f")))
        plats.setPen(QPen(Qt.NoPen))

        self.scene.addItem(plats)

        kolmmeetrit = QGraphicsLineItem(25, 167, 475, 167)
        kolmmeetrit.setPen(QPen(QColor("white"), 3))

        self.scene.addItem(kolmmeetrit)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
