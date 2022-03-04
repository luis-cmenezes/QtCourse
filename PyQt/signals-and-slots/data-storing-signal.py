import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My app")
        
        self.button = QPushButton("Press me!")
        self.button.setCheckable(True)
        self.button.released.connect(self.the_button_was_checked)
        self.button.setChecked(self.button_is_checked)

        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(400, 300))
        self.setCentralWidget(self.button)
    
    def the_button_was_checked(self):
        self.button_is_checked = self.button.isChecked()

        print('Checked ?', self.button_is_checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
    