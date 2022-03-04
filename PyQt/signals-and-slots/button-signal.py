import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        self.button_is_checked = True

        super().__init__()

        self.setWindowTitle("My app")
        
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.setChecked(self.button_is_checked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(400, 300))
        self.setCentralWidget(button)
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
    