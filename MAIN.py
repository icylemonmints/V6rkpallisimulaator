"""
Töö nimi: Võrkpallirotatsioonide simulaator
Töö tegijad: Maria Alas, Ellen H. Möls
"""

"""Sisaldab MainWindowi, RectangleWidgeti ja Controlsi klasse.
1) MainWindow aitab näidata ning ühendada RectangleWidgeti ja Controlsi klasse.
2) RectangleWidget on visualiseeriv osa, millega ise ei saa interakteerida, kuid mis reageerib
   Controlsist saadud signaalidele.
3) Controls on GUI osa, mis annab võimaluse kasutajal otsida soovitud asetusi."""
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow,
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QGraphicsLineItem, QGraphicsEllipseItem, QGraphicsSimpleTextItem,
    QHBoxLayout, QVBoxLayout,
    QWidget, QPushButton
)
from PySide6.QtGui import QBrush, QPen, QColor
from PySide6.QtCore import Qt, Signal

"""koordinaadid mängijate väljakule asetamiseks"""
asetused = {
    4: (1.5, 2), 3: (4.5, 2), 2: (7.5, 2),
    5: (1.5, 6), 6: (4.5, 6), 1: (7.5, 6)
}
rollid = ["S", "N", "T", "D", "N", "T"]


"""klass, mis loob akna, kust on näha väljakuid ja mängijaid"""
class RectangleWidget(QWidget):
    def __init__(self): # siin meetodis on kõik asjad, mille siia klassi loodud objektid pärivad
        super().__init__()  # RectangleWidget pärib oma ülemklassi QWidgeti __init__() meetodi
        self.S = 50
        self.nihe = 0
        
        self.scene = QGraphicsScene(0, 0, 10*self.S, 10*self.S)   # koht, kus asuvad objektid
        self.view = QGraphicsView(self.scene)   # aken, mille kaudu kasutaja neid objekte näeb
        self.view.setFixedSize(10*self.S + 2*self.S, 10*self.S + 2*self.S)
        
        # väljaku loomine
        self.plats = QGraphicsRectItem(0.5*self.S, 0.5*self.S, 9*self.S, 9*self.S)
        self.plats.setBrush(QBrush(QColor("#cb784f")))
        self.plats.setPen(QPen(Qt.NoPen))
        self.scene.addItem(self.plats)

        # kolmemeetrijoon
        kolmmeetrit = QGraphicsLineItem(0.5*self.S, 0.5*self.S + 3*self.S, 9.5*self.S, 0.5*self.S + 3*self.S)
        kolmmeetrit.setPen(QPen(QColor("white"), 3))
        self.scene.addItem(kolmmeetrit)

        # mängijad kogutakse järjendisse, et oleks hiljem hea neid liigutada
        self.mangijad = []
        for n in range(1, 7):
            roll = rollid[n-1]
            mangija = self.joonista_mangija(roll, n)
            self.mangijad.append(mangija)

        layout = QHBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        
    def joonista_mangija(self, silt, positsioon):
        S = 50
        r = 0.6 * S  # ringi raadius
        x, y = asetused[positsioon]

        ring = QGraphicsEllipseItem(-r, -r, 2*r, 2*r)
        ring.setBrush(QBrush(QColor("#FFFFFF")))
        ring.setPen(QPen(Qt.PenStyle.NoPen))
        ring.setPos((0.5 + x)*S, (0.5 + y)*S)   # paneb paika mängija (ehk ringi keskpaiga) koordinaadid

        tekst = QGraphicsSimpleTextItem(silt, ring)     # on ringi alamobjekt, seega käib ringiga kaasas
        kast = tekst.boundingRect()  # teksti ümber tekib mõtteline ristkülik, muutuja "kast" kirjeldab selle mõõtmeid ja koordinaate ringi suhtes
        tekst.setPos(-kast.width() / 2, -kast.height() / 2)  # seab mõttelise kasti ülemise vasaku nurga koordinaadid nii, et tekst ise jääks ringi keskele

        self.scene.addItem(ring)
        return ring

    def muuda_asetust(self):
        self.nihe = (self.nihe+1) % 6
        for i in range(6):
            x, y = asetused[(i+6-self.nihe)%6+1]
            self.mangijad[i].setPos((0.5 + x)*self.S, (0.5 + y)*self.S)

    def vastuvotu_asendisse(self):
        match self.nihe:
            case 0:
                self.mangijad[0].setPos(self.S*(0.5 + 8.2), self.S*(0.5 + 5.5))
                self.mangijad[1].setPos(self.S*(0.5 + 7), self.S*(0.5 + 5))
                self.mangijad[2].setPos(self.S*(0.5 + 4.5), self.S*(0.5 + 2))
                self.mangijad[3].setPos(self.S*(0.5 + 1), self.S*(0.5 + 3))
                self.mangijad[4].setPos(self.S*(0.5 + 2), self.S*(0.5 + 6))
                self.mangijad[5].setPos(self.S*(0.5 + 4.5), self.S*(0.5 + 7))
            case 1:
                self.mangijad[0].setPos(self.S*(0.5 + 4.8), self.S*(0.5 + 2))
                self.mangijad[1].setPos(self.S*(0.5 + 7.5), self.S*(0.5 + 6))
                self.mangijad[2].setPos(self.S*(0.5 + 7), self.S*(0.5 + 3))
                self.mangijad[3].setPos(self.S*(0.5 + 6), self.S*(0.5 + 1))
                self.mangijad[4].setPos(self.S*(0.5 + 1.5), self.S*(0.5 + 5))
                self.mangijad[5].setPos(self.S*(0.5 + 4.2), self.S*(0.5 + 7.5))
            case 2:
                self.mangijad[0].setPos(self.S*(0.5 + 1.5), self.S*(0.5 + 2.8))
                self.mangijad[1].setPos(self.S*(0.5 + 4), self.S*(0.5 + 7))
                self.mangijad[2].setPos(self.S*(0.5 + 6), self.S*(0.5 + 6.5))
                self.mangijad[3].setPos(self.S*(0.5 + 8), self.S*(0.5 + 5))
                self.mangijad[4].setPos(self.S*(0.5 + 2), self.S*(0.5 + 5))
                self.mangijad[5].setPos(self.S*(0.5 + 1), self.S*(0.5 + 1))
            case 3:
                self.mangijad[0].setPos(self.S*(0.5 + 1), self.S*(0.5 + 1))
                self.mangijad[1].setPos(self.S*(0.5 + 3), self.S*(0.5 + 6.2))
                self.mangijad[2].setPos(self.S*(0.5 + 6), self.S*(0.5 + 6.5))
                self.mangijad[3].setPos(self.S*(0.5 + 8), self.S*(0.5 + 5))
                self.mangijad[4].setPos(self.S*(0.5 + 2), self.S*(0.5 + 4))
                self.mangijad[5].setPos(self.S*(0.5 + 1.5), self.S*(0.5 + 2.5))
            case 4:
                self.mangijad[0].setPos(self.S*(0.5 + 4.5), self.S*(0.5 + 2))
                self.mangijad[1].setPos(self.S*(0.5 + 1.5), self.S*(0.5 + 4))
                self.mangijad[2].setPos(self.S*(0.5 + 3), self.S*(0.5 + 6.5))
                self.mangijad[3].setPos(self.S*(0.5 + 5), self.S*(0.5 + 7.2))
                self.mangijad[4].setPos(self.S*(0.5 + 7.5), self.S*(0.5 + 6))
                self.mangijad[5].setPos(self.S*(0.5 + 8), self.S*(0.5 + 3))
            case 5:
                self.mangijad[0].setPos(self.S*(0.5 + 7), self.S*(0.5 + 2))
                self.mangijad[1].setPos(self.S*(0.5 + 1.8), self.S*(0.5 + 5.5))
                self.mangijad[2].setPos(self.S*(0.5 + 1), self.S*(0.5 + 2))
                self.mangijad[3].setPos(self.S*(0.5 + 3), self.S*(0.5 + 8))
                self.mangijad[4].setPos(self.S*(0.5 + 4.5), self.S*(0.5 + 6))
                self.mangijad[5].setPos(self.S*(0.5 + 7.5), self.S*(0.5 + 6))
            case _:
                pass
        
        print("Läheb vastuvõtma")

"""klass, mis loob akna juhtnuppude näitamiseks.
juhtnupud on ühendatud signaalidega rectanglewidgetis olevate meetoditega"""
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

"""klass, mis loob akna väljaku ja mängijate widgeti ning juhtnuppude widgeti nägemiseks"""
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

"""põhiprogramm, mis käivitab rakenduse"""
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__": main()