from PyQt5 import QtWidgets
from ui_config import Ui_MainWindow

import pyqtgraph as pg
import pyqtgraph.opengl as gl
import numpy as np
import sys

SUPERIOR_LIMIT = 430
INFERIOR_LIMIT = 320
COLORS_DICT = {'above': (1.0,0.0,0.0,1.0), 'below': (0.0,0.0,1.0,0.0), 'normal': (0.0,1.0,0.0,1.0)}

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.ui  = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.graphicsView.setCameraPosition(distance=300)
        self.importFiles()
        self.createScatterObject()
        self.createMeshObject()
    
        self.ui.change_marker_btn.clicked.connect(lambda: self.changeMarker())
        self.isItemVisibile = False
    
    def importFiles(self):
        self.trajectory = []
        with open('PyQtGraph/reduced_trajectory.txt', 'r') as file:
            traj_lines = file.readlines()

        for line in traj_lines:
            coords = (line.split(' '))
            coords = tuple(float(coord) for coord in coords)

            self.trajectory.append(coords)


        acquisition = []
        with open('PyQtGraph/retI-retV-rmsI-rmsV-heatInput-T.txt', 'r') as file:
            acq_lines = file.readlines()

        for line in acq_lines:
            data = (line.split(' '))
            data = [float(n_data) for n_data in data]

            acquisition.append(data)

        self.generateColorList(acquisition)

    def generateColorList(self, acquisition):
        self.color = np.empty((len(acquisition), 4))
        for index, row in enumerate(acquisition):

            current_data = row[4]
            if current_data >= INFERIOR_LIMIT and current_data <= SUPERIOR_LIMIT:
                self.color[index] = (0.0, 1.0, 0.0, 1.0)
            elif current_data > SUPERIOR_LIMIT:
                self.color[index] = (1.0, 0.0, 0.0, 1.0)   
            elif current_data < INFERIOR_LIMIT:
                self.color[index] = (0.0, 0.0, 1.0, 1.0)

    def createScatterObject(self):
        self.scatter_object = gl.GLScatterPlotItem(pos=self.trajectory, size=1, color=self.color, pxMode=False)
    
    def createMeshObject(self):
        self.mesh_objects_list = []

        sphere_mesh = gl.MeshData.sphere(rows=40, cols=40)
        for index, point in enumerate(self.trajectory):
            sphere = gl.GLMeshItem(meshdata=sphere_mesh, smooth=True, color=self.color[index], shader='shaded', glOptions='opaque')
            sphere.translate(point[0], point[1], point[2])

            self.mesh_objects_list.append(sphere)
        
    def setMeshVisibility(self, action):
        if action:
            for sphere in self.mesh_objects_list:
                self.ui.graphicsView.addItem(sphere)
        else:
            for sphere in self.mesh_objects_list:
                self.ui.graphicsView.removeItem(sphere)

    def changeMarker(self):
        if self.isItemVisibile:
            try:
                self.isItemVisibile = False
                self.ui.graphicsView.removeItem(self.scatter_object)
                self.setMeshVisibility(True)
            except:
                pass
        else:
            try:
                self.isItemVisibile = True
                self.ui.graphicsView.addItem(self.scatter_object)
                self.setMeshVisibility(False)
            except:
                pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()