from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

import numpy as np

WINDOW_TITLE = 'Visualizador 3D - LAPROSOLDA'
N_LINES = 50

class DataVisualizer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_window()
        self.set_menu()

    def init_window(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.showMaximized()
    
    def set_menu(self):
        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        file_menu.addAction('Load new trajectory...', self.load_trajectory)
        file_menu.addSeparator()
        file_menu.addAction('Load new acquisition...', self.load_acquisition)

        vis_menu = menu.addMenu("Visualization")
        vis_menu.addAction('Set intervals...', self.set_intervals)
        vis_menu.addSeparator()
        vis_menu.addAction('Set new palette...', self.set_palette)

        export_menu = menu.addMenu("Export")
        export_menu.addAction('Export current visualization...', self.export_visualization)
        export_menu.addSeparator()
        export_menu.addAction('Export merged file...', self.export_file)

        quit_menu = menu.addMenu("Quit")
        quit_menu.addAction('Quit', self.quit)
    
    def load_trajectory(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self, 'Open trajectory file')
        file = open(name[0], 'r')
        
        with file:
            trajectory_lines = file.readlines()

        trajectory = np.loadtxt(trajectory_lines)
        print(trajectory)
    
    def load_acquisition(self):
        print('Loading new acquisition...')

    def set_intervals(self):
        pass

    def set_palette(self):
        pass

    def  export_visualization(self):
        pass

    def export_file(self):
        pass

    def quit(self):
        QCoreApplication.quit()



app = QApplication([])

data_visualizer = DataVisualizer()
data_visualizer.show()

app.exec_()
