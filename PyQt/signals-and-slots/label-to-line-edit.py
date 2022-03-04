from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QWidget, QVBoxLayout

import sys
from random import choice

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()
        self.input = QLineEdit()

        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(400, 300))

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()