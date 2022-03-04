import sys
from random import choice

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

window_titles = [
'My App',
'My App',
'Still My App',
'Still My App',
'What on earth',
'What on earth',
'This is surprising',
'This is surprising',
'Something went wrong'
]

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setMinimumSize(QSize(200, 150))
        self.setMaximumSize(QSize(400, 300))
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        print("Clicked!")
        self.setWindowTitle(choice(window_titles))
    
    def the_window_title_changed(self, new_window_title):
        
        if new_window_title == 'Something went wrong':
            self.button.setEnabled(False)
            self.button.setText('Something bad happened')

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
