from PySide6.QtWidgets import QMainWindow, QHBoxLayout,  QWidget
from PySide6.QtCore import QSize

from views.LeftWindow import LeftWindow
from views.RigthWindow import RigthWindow
from views.CentralWindow import CentralWindow

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Management")
        self.setFixedSize(QSize(1200, 800))

        leftWindow = LeftWindow()
        rithWindow = RigthWindow()
        centralWindow = CentralWindow()

        myUI = QHBoxLayout()
        myUI.addWidget(leftWindow, stretch=1)
        myUI.addWidget(centralWindow, stretch=2)
        myUI.addWidget(rithWindow, stretch=1)

        UIWidget = QWidget()
        UIWidget.setLayout(myUI)
        
        self.setCentralWidget(UIWidget)

