from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap

class LeftWindow(QWidget):

    def __init__(self):
        super().__init__()

        containerVBoxLayout = QVBoxLayout()

        logoLabel = QLabel(self)
        pixmap = QPixmap("assets/logo.png")
        logoLabel.setPixmap(pixmap)
        containerVBoxLayout.addWidget(logoLabel)

        containerVBoxLayout.setAlignment(Qt.AlignTop)
        self.setLayout(containerVBoxLayout)