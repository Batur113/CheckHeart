import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel,QPushButton,QVBoxLayout,QHBoxLayout
from PyQt5.QtCore import Qt
from instructions import *

class MainWindow(QWidget):
    def __init__(self,):
        super().__init__()

    def init_ui(self): 
        self.setWindowTitle(txt_title)   
        self.resize(700,450)

        title = QLabel(txt_hello)
        title.setAlignment(Qt.AlignCenter)

        text = QLabel(txt_instruction)
        text.setWordWrap(True)
        text.setAlignment(Qt.AlignLeft)
        