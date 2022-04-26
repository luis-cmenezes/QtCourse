"""
Demonstration of some of the shader programs included with pyqtgraph that can be 
used to affect the appearance of a surface.
"""

import numpy as np

import pyqtgraph as pg
import pyqtgraph.opengl as gl

app = pg.mkQApp()
w = gl.GLViewWidget()
w.show()

g = gl.GLGridItem()
g.setSize(x=200,y=200,z=5)
w.addItem(g)

trajectory = []
with open('PyQtGraph/reduced_trajectory.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    coords = (line.split(' '))
    coords = [float(coordinate) for coordinate in coords]

    trajectory.append(coords)

md = gl.MeshData.sphere(rows=10, cols=10)
no_color_sphere = gl.GLMeshItem(meshdata=md, smooth=True, shader='shaded', color=(1, 1, 1, 1))

print(trajectory)
for point in trajectory:
    #print(f'Criando nova esfera na coordenada [{point[0]},{point[1]},{point[2]}]')
    sphere = no_color_sphere
    sphere.translate(point[0], point[1], point[2])
    w.addItem(sphere)
    
if __name__ == '__main__':
    pg.exec()
