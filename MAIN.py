# See on projekti põhifail. See kood käivitab hetkel tühja akna.
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QGraphicsLineItem
from PySide6.QtGui import QBrush, QPen, QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Võrkpallirotatsioonid")
        # Create scene
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 450, 450)

        # Create view
        self.view = QGraphicsView(self.scene)
        self.setCentralWidget(self.view)

        # Create volleyball court
        S = 50

        plats = QGraphicsRectItem(0, 0, 9*S, 9*S)
        plats.setBrush(QBrush(QColor("lightgreen")))
        plats.setPen(QPen(Qt.black, 2))

        self.scene.addItem(plats)

        # Fit scene into view
        self.view.fitInView(
            self.scene.sceneRect(),
            Qt.KeepAspectRatio
        )

        self.resize(600, 600)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

"""
#teen kastid ja view'i, mille paneme hiljem windowisse
scene = QGraphicsScene()
view = QGraphicsView(scene)

S = 50
plats = QGraphicsRectItem(0,0,9*S,9*S)
plats.setPos(0,0)
scene.addItem(plats)
plats.setBrush(QBrush(QColor("lightgreen")))
plats.setPen(QPen(Qt.black, 2))

app = QApplication(sys.argv)

view.setWindowTitle("Võrkpallirotatsioonid")
view.resize(600, 600)
window = MainWindow()
window.setCentralWidget(view)
window.resize(600, 600)
window.show()
"""


#window = MainWindow()
#window.setCentralWidget(view)
#window.show()
sys.exit(app.exec())