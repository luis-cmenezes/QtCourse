from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

class MenuConfigurator(object):
    def __init__(self):
        pass

    ################################MÉTODOS DE CONFIGURAÇÃO DO MENU SUPERIOR################################
    def setMenu(self):
        menu = self.menuBar()

        self.setFileMenu(menu)
        self.setVisualizationMenu(menu)
        self.setExportMenu(menu)
        self.setQuitMenu(menu)

    def setFileMenu(self, menu):
        file_menu = menu.addMenu("Arquivo")

        load_traj_action = QAction('Carregar nova trajetória...', self)
        load_traj_action.setStatusTip('Carrega uma nova nuvem de pontos para trajetória')
        load_traj_action.triggered.connect(self.loadTrajectory)
        file_menu.addAction(load_traj_action)

        file_menu.addSeparator()

        load_acqu_action = QAction('Carregar nova aquisição...', self)
        load_acqu_action.setStatusTip('Carrega uma nova nuvem de pontos para aquisição')
        load_acqu_action.triggered.connect(self.loadAcquistion)
        file_menu.addAction(load_acqu_action)
    
    def setVisualizationMenu(self, menu):
        vis_menu = menu.addMenu("Visualização")

        interval_set_action = QAction('Definir intervalos...', self)
        interval_set_action.setStatusTip('Define os intervalos das variáveis análise dos dados')
        interval_set_action.triggered.connect(self.setIntervals)
        vis_menu.addAction(interval_set_action)

        vis_menu.addSeparator()

        palette_set_action = QAction('Definir nova paleta....', self)
        palette_set_action.setStatusTip('Define a paleta de cores utilizada na visualização dos dados')
        palette_set_action.triggered.connect(self.setPalette)
        vis_menu.addAction(palette_set_action)
    
    def setExportMenu(self, menu):
        export_menu = menu.addMenu("Exportar")

        export_vis_action = QAction('Exportar visualização atual...', self)
        export_vis_action.setStatusTip('Exporta a visualição como está agora para um arquivo de imagem')
        export_vis_action.triggered.connect(self.exportVisualization)
        export_menu.addAction(export_vis_action)

        export_menu.addSeparator()

        export_file_action = QAction('Exportar arquivo mesclado...', self)
        export_file_action.setStatusTip('Exporta o arquivo gerado pelo correlacionamento da trajetória com a aquisição')
        export_file_action.triggered.connect(self.exportFile)
        export_menu.addAction(export_file_action)
    
    def setQuitMenu(self, menu):
        quit_menu = menu.addMenu("Sair")
        quit_menu.addAction('Sair', self.quit)

    ################################MÉTODOS DE REAÇÃO ÀS OPÇÕES DO MENU SUPERIOR################################
    def setIntervals(self):
        pass

    def setPalette(self):
        pass

    def exportVisualization(self):
        pass

    def exportFile(self):
        pass

    def quit(self):
        QCoreApplication.quit()