SUPERIOR_LIMIT = 430
INFERIOR_LIMIT = 320
COLORS_DICT = {'above': (1.0,0.0,0.0,1.0), 'below': (0.0,0.0,1.0,0.0), 'normal': (0.0,1.0,0.0,1.0)}

import numpy as np

import pyqtgraph as pg
import pyqtgraph.opengl as gl
from pyqtgraph.Qt import QtCore

app = pg.mkQApp()
w = gl.GLViewWidget()
w.show()
w.setCameraPosition(distance=300)


trajectory = []
with open('PyQtGraph/reduced_trajectory.txt', 'r') as file:
    traj_lines = file.readlines()

for line in traj_lines:
    coords = (line.split(' '))
    coords = tuple(float(coord) for coord in coords)

    trajectory.append(coords)


acquisition = []
with open('PyQtGraph/retI-retV-rmsI-rmsV-heatInput-T.txt', 'r') as file:
    acq_lines = file.readlines()

for line in acq_lines:
    data = (line.split(' '))
    data = [float(n_data) for n_data in data]

    acquisition.append(data)

color = np.empty((len(acquisition), 4))
for index, row in enumerate(acquisition):

    current_data = row[4]
    if current_data > INFERIOR_LIMIT and current_data < SUPERIOR_LIMIT:
        color[index] = (0.0, 1.0, 0.0, 1.0)
    elif current_data >= SUPERIOR_LIMIT:
        color[index] = (1.0, 0.0, 0.0, 1.0)   
    elif current_data <= INFERIOR_LIMIT:
        color[index] = (0.0, 0.0, 1.0, 1.0)

sphere_mesh = gl.MeshData.sphere(rows=10, cols=10)
for index, point in enumerate(trajectory):
    sphere = gl.GLMeshItem(meshdata=sphere_mesh, smooth=False, color=color[index], shader='shaded', glOptions='opaque')
    sphere.translate(point[0], point[1], point[2])
    w.addItem(sphere)


if __name__ == '__main__':
    pg.exec()
