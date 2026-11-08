import sys
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow,
    QGraphicsScene, QGraphicsView,
    QGraphicsRectItem, QGraphicsLineItem, QPushButton, QVBoxLayout, QWidget
)
from PySide6.QtGui import QBrush, QPen, QColor
from PySide6.QtCore import Qt
from PySide6.QtCore import Signal

"""
Vaja
1) buttonite ja teksti widget
2) platsi widget
3) ühendada need omavahel
"""
class RectangleWidget(QWidget):
    def __init__(self):
        super().__init__()
        S = 50
        layout = QHBoxLayout()

        self.scene = QGraphicsScene(0,0, 10*S, 10*S)
        self.view = QGraphicsView(self.scene)
        self.view.setFixedSize(10*S + 2*S, 10*S + 2*S)
        #loon väljakuala
        self.plats = QGraphicsRectItem(0.5*S, 0.5*S, 9*S, 9*S)
        self.plats.setBrush(QBrush(QColor("#cb784f")))
        self.plats.setPen(QPen(Qt.NoPen))

        self.scene.addItem(self.plats)
        #loon kolmemeetrise joone
        self.kolmmeetrit = QGraphicsLineItem(0.5*S, 0.5*S + 3*S, 9.5*S, 0.5*S + 3*S)
        self.kolmmeetrit.setPen(QPen(QColor("white"), 3))
        
        self.scene.addItem(self.kolmmeetrit)


        layout.addWidget(self.view)
        self.setLayout(layout)

    def muudaplatsi(self):
        praegune_platsivärv = self.plats.brush().color()
        if praegune_platsivärv == QColor("#cb784f"):
            self.plats.setBrush(QBrush(QColor("#dfb49f")))

        else:
            self.plats.setBrush(QBrush(QColor("#cb784f")))

class MainWindow(QMainWindow):
    def __init__(self):
            super().__init__()
            self.setWindowTitle("Võrkpallirotatsioonide simulaator")

            self.rectangle_widget = RectangleWidget()
            self.controls_widget = controls(self.rectangle_widget)
            self.controls_widget.setFixedWidth(200)

            self.controls_widget.platsi_muutus.connect(
            self.rectangle_widget.muudaplatsi)

            näidatavWidget = QWidget()
            layout = QHBoxLayout(näidatavWidget)
            layout.addStretch(1)
            layout.addWidget(self.rectangle_widget,0)
            layout.addWidget(self.controls_widget)
            layout.addStretch(1)
            self.setCentralWidget(näidatavWidget)

class controls(QWidget):
    platsi_muutus = Signal()
    def __init__(self, rectangle_widget):
        super().__init__()
        self.rectangle_widget = rectangle_widget
        layout = QVBoxLayout(self)

        self.muuda_platsi_nupp = QPushButton("Muuda platsi värvi")
        self.muuda_platsi_nupp.clicked.connect(self.platsi_muutus.emit)


        layout.addWidget(self.muuda_platsi_nupp, alignment=Qt.AlignHCenter)
        self.setLayout(layout)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
