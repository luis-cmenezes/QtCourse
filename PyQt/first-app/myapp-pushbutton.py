from PyQt5.QtWidgets import QApplication, QPushButton

app = QApplication([])

window = QPushButton("Push me!")
window.show()

app.exec_()