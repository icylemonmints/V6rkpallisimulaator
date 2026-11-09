# See on projekti põhifail.
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QGraphicsLineItem, QGraphicsEllipseItem, QGraphicsSimpleTextItem,
    QHBoxLayout, QVBoxLayout,
    QWidget, QPushButton
)
from PySide6.QtGui import QBrush, QPen, QColor
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal

asetused = {
    4: (1.5, 2), 3: (4.5, 2), 2: (7.5, 2),
    5: (1.5, 6), 6: (4.5, 6), 1: (7.5, 6)
}
rollid = ["S", "T", "N", "D", "T", "N"]

class RectangleWidget(QWidget):
    def __init__(self):
        super().__init__()
        S = 50
        layout = QHBoxLayout()
        
        self.scene = QGraphicsScene(0, 0, 10*S, 10*S)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(10*S + 2*S, 10*S + 2*S)
        
        #loon väljakuala
        self.plats = QGraphicsRectItem(0.5*S, 0.5*S, 9*S, 9*S)
        self.plats.setBrush(QBrush(QColor("#cb784f")))
        self.plats.setPen(QPen(Qt.NoPen))

        self.scene.addItem(self.plats)

        # kolmemeetrijoon
        kolmmeetrit = QGraphicsLineItem(0.5*S, 0.5*S + 3*S, 9.5*S, 0.5*S + 3*S)
        kolmmeetrit.setPen(QPen(QColor("white"), 3))
        
        self.scene.addItem(kolmmeetrit)

        self.players = [self.joonista_mangija(str(rollid[n-1]), n) for n in range(1, 7)]

        layout.addWidget(self.view)
        self.setLayout(layout)
        
    def joonista_mangija(self, silt, positsioon):
        S = 50  # kas peaks tegema S = self.S ning muutma ka initis ära?
        r = 0.5 * S  # ringi raadius
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

    def muuda_asetust(self):
        print("Liigub edasi")

    def vastuvotu_asendisse(self):
        print("Läheb vastuvõtma")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Võrkpallirotatsioonide simulaator")

        self.valjak = RectangleWidget()  
        self.juhtimine = controls(self.valjak)
        self.juhtimine.setFixedWidth(200)

        self.juhtimine.edasi.connect(self.valjak.muuda_asetust)
        self.juhtimine.vastuvottu.connect(self.valjak.vastuvotu_asendisse)

        näidatavWidget = QWidget()
        layout = QHBoxLayout(näidatavWidget)
        layout.addStretch(1)
        layout.addWidget(self.valjak,0)
        layout.addWidget(self.juhtimine)
        layout.addStretch(1)
        self.setCentralWidget(näidatavWidget)

class controls(QWidget):
    edasi = Signal()
    vastuvottu = Signal()
    def __init__(self, valjak):
        super().__init__()
        self.valjak = valjak 
        layout = QVBoxLayout(self)

        self.roteeru = QPushButton("Rotatsioon edasi")
        self.roteeru.clicked.connect(self.edasi.emit)

        self.vastuvott = QPushButton("Vastuvõtu asendisse")
        self.vastuvott.clicked.connect(self.vastuvottu.emit)

        layout.addWidget(self.roteeru)
        layout.addWidget(self.vastuvott)
        self.setLayout(layout)

    


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
