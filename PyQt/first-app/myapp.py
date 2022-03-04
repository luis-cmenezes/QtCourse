from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])

window = QWidget()
window.show()

window2 = QPushButton("Push me!")
window2.show()

app.exec_()