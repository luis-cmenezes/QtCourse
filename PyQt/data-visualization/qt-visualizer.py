from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

import time

WINDOW_TITLE = 'Visualizador 3D - LAPROSOLDA'

class DataVisualizer(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_window()
        self.set_menu()
        self.setStatusBar(QStatusBar(self))

    def init_window(self):
        self.setWindowTitle(WINDOW_TITLE)
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.showMaximized()
        self.loading_bar = QProgressBar(self)
        self.setCentralWidget(self.loading_bar)
    
    ################################MÉTODOS DE CONFIGURAÇÃO DO MENU SUPERIOR################################
    def set_menu(self):
        menu = self.menuBar()

        self.set_file_menu(menu)
        self.set_visualization_menu(menu)
        self.set_export_menu(menu)
        self.set_quit_menu(menu)

    def set_file_menu(self, menu):
        file_menu = menu.addMenu("Arquivo")

        load_traj_action = QAction('Carregar nova trajetória...', self)
        load_traj_action.setStatusTip('Carrega uma nova nuvem de pontos para trajetória')
        load_traj_action.triggered.connect(self.load_trajectory)
        file_menu.addAction(load_traj_action)

        file_menu.addSeparator()

        load_acqu_action = QAction('Carregar nova aquisição...', self)
        load_acqu_action.setStatusTip('Carrega uma nova nuvem de pontos para aquisição')
        load_acqu_action.triggered.connect(self.load_acquisition)
        file_menu.addAction(load_acqu_action)
    
    def set_visualization_menu(self, menu):
        vis_menu = menu.addMenu("Visualização")

        interval_set_action = QAction('Definir intervalos...', self)
        interval_set_action.setStatusTip('Define os intervalos das variáveis análise dos dados')
        interval_set_action.triggered.connect(self.set_intervals)
        vis_menu.addAction(interval_set_action)

        vis_menu.addSeparator()

        palette_set_action = QAction('Definir nova paleta....', self)
        palette_set_action.setStatusTip('Define a paleta de cores utilizada na visualização dos dados')
        palette_set_action.triggered.connect(self.set_palette)
        vis_menu.addAction(palette_set_action)
    
    def set_export_menu(self, menu):
        export_menu = menu.addMenu("Exportar")

        export_vis_action = QAction('Exportar visualização atual...', self)
        export_vis_action.setStatusTip('Exporta a visualição como está agora para um arquivo de imagem')
        export_vis_action.triggered.connect(self.export_visualization)
        export_menu.addAction(export_vis_action)

        export_menu.addSeparator()

        export_file_action = QAction('Exportar arquivo mesclado...', self)
        export_file_action.setStatusTip('Exporta o arquivo gerado pelo correlacionamento da trajetória com a aquisição')
        export_file_action.triggered.connect(self.export_file)
        export_menu.addAction(export_file_action)
    
    def set_quit_menu(self, menu):
        quit_menu = menu.addMenu("Sair")
        quit_menu.addAction('Sair', self.quit)

    ################################MÉTODOS DE REAÇÃO ÀS OPÇÕES DO MENU SUPERIOR################################
    def load_trajectory(self):
        self.trajectory = []
        f_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir arquivo de trajetória')[0]

        with open(f_name, 'r') as file:
            lines = file.readlines()

        size = len(lines)
        for i, line in enumerate(lines):
            self.loading_bar.setValue(int(100*i/size)+1)
            coords = (line.split(' '))
            coords = [float(coordinate) for coordinate in coords]

            self.trajectory.append(coords)
            
    def load_acquisition(self):
        self.acquisition = []
        f_name = QtWidgets.QFileDialog.getOpenFileName(self, 'Abrir arquivo de aquisição')[0]

        with open(f_name, 'r') as file:
            lines = file.readlines()

        size = len(lines)
        for i, line in enumerate(lines):
            self.loading_bar.setValue(int(100*i/size)+1)
            data = (line.split(' '))
            data = [float(n_data) for n_data in data]

            self.acquisition.append(data)

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

if __name__ == '__main__':
    app = QApplication([])

    data_visualizer = DataVisualizer()
    data_visualizer.show()

    app.exec_()
