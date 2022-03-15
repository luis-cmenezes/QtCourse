import sys

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout

from layout_color_widget import Color

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(1, 1, 1, 1)
        layout1.setSpacing(1)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)
        
        layout1.addWidget(Color('green'))
        layout1.addWidget(Color('gray'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
    

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
    