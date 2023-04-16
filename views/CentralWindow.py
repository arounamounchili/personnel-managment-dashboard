from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import Qt

class CentralWindow(QWidget):

    def __init__(self):
        super().__init__()

        containerVBoxLayout = QVBoxLayout()

        self.setLayout(containerVBoxLayout)
