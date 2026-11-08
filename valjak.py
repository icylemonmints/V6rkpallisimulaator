import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QGraphicsLineItem, QGraphicsEllipseItem, QGraphicsSimpleTextItem
)
from PySide6.QtGui import QBrush, QPen, QColor
from PySide6.QtCore import Qt

asetused = {
    4: (1.5, 2), 3: (4.5, 2), 2: (7.5, 2),
    5: (1.5, 6), 6: (4.5, 6), 1: (7.5, 6)
}
rollid = ["S", "T", "N", "D", "T", "N"]

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

        kolmmeetrit = QGraphicsLineItem(0.5*S, 0.5*S + 3*S, 9.5*S, 0.5*S + 3*S)
        kolmmeetrit.setPen(QPen(QColor("white"), 3))

        self.scene.addItem(kolmmeetrit)

        self.players = [self.joonista_mangija(str(rollid[n-1]), n) for n in range(1, 7)]

    def joonista_mangija(self, silt, positsioon):
        S = 50  # kas peaks tegema S = self.S ning muutma ka initis ära?
        r = 0.5 * S  #ringi raadius
        x, y = asetused[positsioon]

        ring = QGraphicsEllipseItem(-r, -r, 2*r, 2*r)
        ring.setBrush(QBrush(QColor("#FFFFFF")))
        ring.setPen(QPen(Qt.PenStyle.NoPen))
        ring.setPos((0.5 + x)*S, (0.5 + y)*S)

        tekst = QGraphicsSimpleTextItem(silt, ring)     # on ringi "laps", seega käib ringiga kaasas
        box = tekst.boundingRect()
        tekst.setPos(-box.width() / 2, -box.height() / 2)  # paneb teksti ringi keskele kuidagi

        self.scene.addItem(ring)
        return ring


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
