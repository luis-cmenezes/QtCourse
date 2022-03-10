from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from menu_config import MenuConfigurator

import time

WINDOW_TITLE = 'Visualizador 3D - LAPROSOLDA'

class DataVisualizer(QMainWindow, MenuConfigurator):

    def __init__(self):
        super().__init__()

        self.setMenu()
        self.initWindow()
        self.trajectory_table = QTableWidget(0,0)
        self.acquisition_table = QTableWidget(0,0)

        layout = QHBoxLayout()
        layout.addWidget(self.trajectory_table)
        layout.addWidget(self.acquisition_table)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def initWindow(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.showMaximized()
    
    def loadTrajectory(self):
        self.trajectory = []
        f_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir arquivo de trajetória')[0]

        with open(f_name, 'r') as file:
            lines = file.readlines()

        size = len(lines)
        for i, line in enumerate(lines):
            coords = (line.split(' '))
            coords = [float(coordinate) for coordinate in coords]

            self.trajectory.append(coords)
        
        self.trajectory_table.setColumnCount(len(self.trajectory[0]))
        self.trajectory_table.setRowCount(200)
        self.trajectory_table.setHorizontalHeaderLabels(['Clique duplo para renomear']*3)
        self.trajectory_table.horizontalHeader().sectionDoubleClicked.connect(self.changeTrajHorHeader)

        for i, line in enumerate(self.trajectory):
            if i > 200:
                break
            for j, coord in enumerate(line):
                object = QTableWidgetItem(str(coord))
                object.setTextAlignment(Qt.AlignCenter)
                self.trajectory_table.setItem(i, j, object)
    
    def loadAcquistion(self):
        self.acquisition = []
        f_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir arquivo de aquisição')[0]

        with open(f_name, 'r') as file:
            lines = file.readlines()

        size = len(lines)
        for i, line in enumerate(lines):
            data = (line.split(' '))
            data = [float(n_data) for n_data in data]

            self.acquisition.append(data)
        
        self.acquisition_table.setColumnCount(len(self.acquisition[0]))
        self.acquisition_table.setRowCount(200)
        self.acquisition_table.setHorizontalHeaderLabels(['Clique duplo para renomear']*6)
        self.acquisition_table.horizontalHeader().sectionDoubleClicked.connect(self.changeAcqHorHeader)

        for i, line in enumerate(self.acquisition):
            if i > 200:
                break
            for j, coord in enumerate(line):
                object = QTableWidgetItem(str(coord))
                object.setTextAlignment(Qt.AlignCenter)
                self.acquisition_table.setItem(i, j, object)

    def changeTrajHorHeader(self, index):
        it = self.trajectory_table.horizontalHeaderItem(index)
        newHeader, okPressed  = QtWidgets.QInputDialog.getText(self,
            ' Nomear variável', 'Nome da variável: ', 
            QtWidgets.QLineEdit.Normal)
        if okPressed:
            it.setText(newHeader)
    
    def changeAcqHorHeader(self, index):
        it = self.acquisition_table.horizontalHeaderItem(index)
        newHeader, okPressed  = QtWidgets.QInputDialog.getText(self,
            ' Nomear variável', 'Nome da variável: ', 
            QtWidgets.QLineEdit.Normal)
        if okPressed:
            it.setText(newHeader)

if __name__ == '__main__':
    app = QApplication([])

    data_visualizer = DataVisualizer()
    data_visualizer.show()

    app.exec_()
