import sys
from PySide6.QtWidgets import (QApplication, QGraphicsScene, QGraphicsView,
                               QGraphicsEllipseItem)
from PySide6.QtGui import QBrush, QColor, QPen
from PySide6.QtCore import Qt

S = 40  # pixels per meter

app = QApplication(sys.argv)
scene = QGraphicsScene()

# Court: 18 m x 9 m
scene.addRect(0, 0, 9 * S, 9 * S, QPen(Qt.white, 3), QBrush(QColor("#e8a85c")))

view = QGraphicsView(scene)
view.show()
sys.exit(app.exec())