
import sys
import matplotlib
import platform
import os

from matplotlib import cm
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
from matplotlib.animation import FuncAnimation

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot

import warnings
warnings.filterwarnings('ignore')
from app_modules import *
class Display(FigureCanvas):
    def __init__(self,parent=None, width = 70, height = 50,dpi=75):
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#343b48')
        figure.suptitle('3D Robotics Simulation',color='white',fontsize=15)
        style.use("seaborn-notebook")
        #self.axes = figure.add_subplot(111,projection='3d')
        self.axes = figure.gca(projection='3d')
        figure.tight_layout()
        super(Display, self).__init__(figure)
    def config_display(self):
        self.axes.set_facecolor('#343b48')
        self.axes.grid(True)
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

        self.screen = Display(self,width=50, height=50, dpi=70)
        self.screen.config_display()
        self.ui.screen_form.addWidget(self.screen)

        self.ui.btn_Setting.clicked.connect(lambda: UIFunctions.toggleMenu_setting(self,280,True))
        self.ui.the1_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.btn_plus.clicked.connect(lambda: UIFunctions.timechange_plus(self))
        self.ui.btn_minus.clicked.connect(lambda: UIFunctions.timechange_minus(self))
        self.ui.btn_reset.clicked.connect(lambda: UIFunctions.reset(self))

        ## Mouse Clicked and Keyboard Event ##
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            UIFunctions.reset(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
