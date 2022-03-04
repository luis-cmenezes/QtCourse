import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(400, 300))
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me!")
        self.button.setEnabled(False)

        self.setWindowTitle("Oneshot App")
    
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()