#From https://stackoverflow.com/questions/45369725/how-to-use-matplotlib-with-pyqt4
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class Canvas(FigureCanvas):
    def __init__(self, parent=None):
        self.figure = plt.figure()
        FigureCanvas.__init__(self, self.figure)
        self.setParent(parent)
