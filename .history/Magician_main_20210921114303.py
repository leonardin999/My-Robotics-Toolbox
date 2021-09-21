
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
    def config_display(self,widget):
        widget.axes.set_facecolor('#343b48')
        widget.axes.grid(True)
        widget.axes.set_xlim(10,-45)
        widget.axes.set_ylim(-35, 35)
        widget.axes.set_zlim(-5, 35)

        widget.axes.set_xlabel('X_axis',color='white',fontsize=10)
        widget.axes.set_ylabel('Y_axis',color='white',fontsize=10)
        widget.axes.set_zlabel('Z_axis',color='white',fontsize=10)
        widget.axes.tick_params(axis='x', colors='white')
        widget.axes.tick_params(axis='y', colors='white')
        widget.axes.tick_params(axis='z', colors='white')
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi('Display_setting/Magician_Display.ui',self)
        #self.ui.setupUi(self)
        print('System: '+platform.system())
        print('Version: '+platform.release())
        UIFunctions.uiDefinitions(self)

        self.screen = Display(self,width=50, height=50, dpi=70)
        self.screen.config_display(self.screen)
        self.ui.screen_form.addWidget(self.screen)

        self.ui.btn_Setting.clicked.connect(lambda: UIFunctions.toggleMenu_setting(self,280,True))
        self.ui.the1_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.btn_plus.clicked.connect(lambda: UIFunctions.timechange_plus(self))
        self.ui.btn_minus.clicked.connect(lambda: UIFunctions.timechange_minus(self))
        self.ui.btn_reset.clicked.connect(lambda: UIFunctions.reset(self))

        ## initialize parameter:
        self.length1.setText('50')
        self.length2.setText('40')
        self.length3.setText('30')
        self.link = [float(self.length1.text()),
                     float(self.length2.text()),
                     float(self.length3.text())]
        Userfunctions.initialize_robot(self,self.link)

        ## Realtime Display Event:

        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(lambda: Userfunctions.Geometry_display(self))
        #self.timer.start(100)

        ## Mouse Clicked and Keyboard Event ##
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.RightButton:
            UIFunctions.reset(self)
        if event.buttons() == Qt.MidButton:
            UIFunctions.Update_value(self)

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
        if event.key() == Qt.Key_R:
            self.ui.length1.setText('50')
            self.ui.length2.setText('40')
            self.ui.length3.setText('30')
            self.link = [float(self.length1.text()),
                         float(self.length2.text()),
                         float(self.length3.text())]
            Userfunctions.initialize_robot(self,self.link)
        if event.key() == Qt.Key_Enter:
            Userfunctions.Geometry_display(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
