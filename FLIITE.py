import sys
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import queue
import numpy as np
import pdb
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSlot

import matplotlib
matplotlib.use('QT5Agg')
import matplotlib.pylab as plt


### GLOBAL VARIABLES START ###

### GLOBAL VARIABLES END ###

class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
            fig = Figure(figsize=(width, height), dpi=dpi)
            self.ax = fig.add_subplot(111)
            super().__init__(fig)
            self.setParent(parent)

            """ 
            Matplotlib Script
            """
            t = np.arange(0.0, 2.0, 0.01)
            s = 1 + np.sin(2 * np.pi * t)
            
            self.ax.plot(t, s)

            self.ax.set(xlabel='time (s)', ylabel='voltage (mV)',
                title='About as simple as it gets, folks')
            self.ax.grid()
            fig.tight_layout()


# this class id the big kahuna who runs the show
# TODO: connect functions to interactable components and figure the rest out too
class PyShine_LIVE_PLOT_APP(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('GSApp.ui',self)
        self.resize(888, 600)

        ### PLOTTING START ###
        self.canvas = Canvas(self, width=5, height=4, dpi=100)
        self.ui.gridLayout_3.addWidget(self.canvas,0,0)
        ### PLOTTING END ###

        ### BUTTON BINDINGS START ###
        self.loadDataButton.clicked.connect(self.load_data)
        ### BUTTON BINDINGS END ###
    
    def load_data(self):
        filename = QFileDialog.getOpenFileName()[0]
        print(filename)
        f = open(filename, 'r')

        
    

app = QtWidgets.QApplication(sys.argv)
mainWindow = PyShine_LIVE_PLOT_APP()
mainWindow.show()
sys.exit(app.exec_())