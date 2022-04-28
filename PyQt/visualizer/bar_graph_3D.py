import sys, csv
import numpy as np

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtDataVisualization import Q3DBars, QBarDataItem, QBar3DSeries, QValue3DAxis, Q3DCamera
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class SimpleBarGraph(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()
    
    def initializeUI(self):
        self.setMinimumSize(800,700)
        self.setWindowTitle('3D Bar Graph')

        self.setupGraph()
        self.show()
    
    def setupGraph(self):
        header_label = QLabel("Average Monthly Temperatures in Reykjavík, Iceland 1990-2000 (°C)")
        header_label.setAlignment(Qt.AlignCenter)

        temperature_data = self.loadCSVFile()

        rows, columns = temperature_data.shape
        years = temperature_data[rows-11:rows,1]
        monthly_temps = temperature_data[rows - 11:rows, 2:columns-1].astype(float)

        bar_graph = Q3DBars()
        #bar_graph.scene().activateCamera().setCameraPreset(Q3DCamera.CameraPresetFront)

        data_itens = []

        for row in monthly_temps:
            data_itens.append([QBarDataItem(value) for value in row])
        
        months = ["January", "February", "March", "April", "May", "June", 
        "July", "August", "September", "October", "November", "December"]

        series = QBar3DSeries()
        series.setBaseColor(QColor("#17A4D9"))
        series.setSingleHighlightColor(QColor("#F8A307"))
        series.dataProxy().addRows(data_itens)
        series.dataProxy().setRowLabels(years)
        series.dataProxy().setColumnLabels(months)

        temperature_axis = QValue3DAxis()
        temperature_axis.setRange(-10,20)
        temperature_axis.setLabelFormat(u"%.1f \N{degree sign}C")
        bar_graph.setValueAxis(temperature_axis)

        series.setItemLabelFormat("Reykjavík - @colLabel @rowLabel: @valueLabel")
        
        bar_graph.addSeries(series)

        container = self.createWindowContainer(bar_graph)
        v_box = QVBoxLayout()
        v_box.addWidget(header_label)
        v_box.addWidget(container, 1)
        self.setLayout(v_box)

    def loadCSVFile(self):
        file_name = 'visualizer/Reykjavik_temp.csv'

        with open(file_name, "r") as csv_f:
            reader = csv.reader(csv_f)
            header_labels = next(reader)
            data = np.array(list(reader))
        
        return data

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleBarGraph()
    sys.exit(app.exec_())