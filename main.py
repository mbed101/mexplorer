#!/usr/bin/env python3

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QVBoxLayout, QWidget,QLineEdit,QGraphicsView,QTreeView, QFileSystemModel
import PySide6.QtCore 
from PySide6.QtGui import QFont, QIntValidator, QPainter
from PySide6.QtCore import QTimer,  QDir
from PySide6.QtCharts import QChart, QLineSeries, QChartView, QCandlestickSeries,QCandlestickSet
import json

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # load settings 
        #self.settings_file_name = 'settings.json'
        #self.settings = self.load_settings(self.settings_file_name)
        
        self.setWindowTitle("MExplorer")
        self.showMaximized()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QHBoxLayout()
        central_widget.setLayout(layout)

        self.current_path = "."
        self.label = QLabel(self.current_path, self)
        self.label.setAlignment(PySide6.QtCore.Qt.AlignTop)
        font = QFont("Arial", 20)
        self.label.setFont(font)

        layout.addWidget(self.label)

         # Create a QTreeView
        self.ltree_view = QTreeView(self)

        # Create a QFileSystemModel to display the file system
        lmodel = QFileSystemModel()
        lmodel.setRootPath(QDir.homePath())

        # Set the model for the tree view
        self.ltree_view.setModel(lmodel)
        self.ltree_view.setRootIndex(lmodel.index(QDir.homePath()))  # Set the root index

        layout.addWidget(self.ltree_view)

        # Right tab
        self.rtree_view = QTreeView(self)

        # Create a QFileSystemModel to display the file system
        rmodel = QFileSystemModel()
        rmodel.setRootPath(QDir.homePath())  # Set the root path to display

        # Set the model for the tree view
        self.rtree_view.setModel(rmodel)
        self.rtree_view.setRootIndex(rmodel.index(QDir.homePath()))  # Set the root index
        layout.addWidget(self.rtree_view)


    def save_settings(self,settings, file_path):
        with open(file_path, 'w') as config_file:
            json.dump(settings, config_file, indent=4)

    def load_settings(self,file_path):
        with open(file_path,'r') as config_file:
            settings=json.load(config_file)
        return settings

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())


