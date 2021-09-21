
import platform
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
## import Matplotlib in Pyqt5
import matplotlib
from matplotlib import style
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as Canvas
from matplotlib.animation import FuncAnimation
from app_modules import *
class Display(Canvas):
    def __init__(self,parent=None, width = 15, height = 4,dpi=100):
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#343b48')
        figure.suptitle('3D Robotics Simulation',color='white',fontsize=15)
        style.use("seaborn-notebook")
        figure.tight_layout()
        self.axes = figure.gca(projection='3d')
        super(Display, self).__init__(figure)
    def config_display(self):
        self.axes.set_facecolor('#343b48')
        self.axes.set_xlim(10,-45)
        self.axes.set_ylim(-35, 35)
        self.axes.set_zlim(-5, 35)

        self.axes.set_xlabel('X_axis',color='white',fontsize=10)
        self.axes.set_ylabel('Y_axis',color='white',fontsize=10)
        self.axes.set_zlabel('Z_axis',color='white',fontsize=10)
        self.axes.tick_params(axis='x', colors='white')
        self.axes.tick_params(axis='y', colors='white')
        self.axes.tick_params(axis='z', colors='white')
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi('Display_setting/Magician_Display.ui',self)
        #self.ui.setupUi(self)
        print('System: '+platform.system())
        print('Version: '+platform.release())
        UIFunctions.uiDefinitions(self)

        self.screen = Display(self)
        self.screen.config_display()

        self.ui.btn_Setting.clicked.connect(lambda: UIFunctions.toggleMenu_setting(self,280,True))
        self.ui.the1_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.btn_plus.clicked.connect(lambda: UIFunctions.timechange_plus(self))
        self.ui.btn_minus.clicked.connect(lambda: UIFunctions.timechange_minus(self))
        self.ui.btn_reset.clicked.connect(lambda: UIFunctions.reset(self))

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
