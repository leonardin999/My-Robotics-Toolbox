
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

        ## initializing Threading Core
        self.threadpool = QtCore.QThreadPool()
        ## initialize parameter:
        self.link = [float(self.length1.text()),
                     float(self.length2.text()),
                     float(self.length3.text())]
        Userfunctions.initialize_robot(self,self.link)

        self.screen = Display(self,width=50, height=50, dpi=70)
        self.screen.config_display(self.screen)
        self.ui.screen_form.addWidget(self.screen)

        self.ui.btn_Setting.clicked.connect(lambda: UIFunctions.toggleMenu_setting(self,280,True))
        self.ui.the1_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the1_adjust.valueChanged.connect(lambda: Userfunctions.Geometry_display(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the2_adjust.valueChanged.connect(lambda: Userfunctions.Geometry_display(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: UIFunctions.valuechange(self))
        self.ui.the3_adjust.valueChanged.connect(lambda: Userfunctions.Geometry_display(self))
        self.ui.btn_plus.clicked.connect(lambda: UIFunctions.timechange_plus(self))
        self.ui.btn_minus.clicked.connect(lambda: UIFunctions.timechange_minus(self))
        self.ui.btn_reset.clicked.connect(lambda: Userfunctions.link_adjustment(self))
        self.ui.btn_home.clicked.connect(lambda: Userfunctions.Home_position(self))

        ## button simulation mode
        self.ui.btn_start.clicked.connect(lambda: Userfunctions.start_process(self))
        self.ui.mode_check.stateChanged.connect(lambda: UIFunctions.simulation_check(self))
        ## Realtime Display Event:

        #self.timer = QtCore.QTimer()
        #self.timer.timeout.connect(lambda: Userfunctions.Geometry_display(self))
        #self.timer.start(100)

        ## Mouse Clicked and Keyboard Event ##
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.RightButton:
            pass
        if event.buttons() == Qt.MidButton:
            UIFunctions.Update_value(self)

    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
        if event.key() == Qt.Key_R:
            UIFunctions.reset(self)

    def start_simulation_mode(self):
        self.active = True
        worker = Worker(lambda: self.Trajectory())
        self.threadpool.start(worker)

    def stop_simulation_mode(self):
        self.active = False
        time.sleep(0.3)

    def Trajectory(self):
        time = self.ui.time_respond.text().split()
        compare = int(time[0])
        self.idx=0
        while self.ui.mode_check.isChecked() and self.idx <= compare*10-30 and self.active == True:
            try:
                value_1 = np.round(float(self.ui.the1_current.text()),2)
                value_2 = np.round(float(self.ui.the2_current.text()),2)
                value_3 = np.round(float(self.ui.the3_current.text()),2)
                the = np.array([value_1,value_2,value_3])
                time = self.time_respond.text().split()
                tc = int(time[0])

                a1 = self.the1pre
                b1 = 0
                c1 = 3 * (the[0]- self.the1pre) / tc ** 2
                d1 = -2 * (the[0] - self.the1pre) / tc ** 3

                a2 = self.the2pre
                b2 = 0
                c2 = 3 * (the[1]- self.the2pre) / tc ** 2
                d2 = -2 * (the[1]- self.the2pre) / tc ** 3

                a3 = self.the3pre
                b3 = 0
                c3 = 3 * (the[2] - self.the3pre) / tc ** 2
                d3 = -2 * (the[2] - self.the3pre) / tc ** 3

                self.the1_flex = np.round(a1 + b1 * self.idx / 10 + c1 * (self.idx / 10) * 2 + d1 * (self.idx / 10) * 3, 4)
                self.the2_flex = np.round(a2 + b2 * self.idx / 10 + c2 * (self.idx / 10) * 2 + d2 * (self.idx / 10) * 3, 4)
                self.the3_flex = np.round(a3 + b3 * self.idx / 10 + c3 * (self.idx / 10) * 2 + d3 * (self.idx / 10) * 3, 4)

                theta_flex = np.array([self.the1_flex,self.the2_flex,self.the3_flex])
                self.ui.the1_current.setText(str(Userfunctions.convert_to_Deg(theta_flex[0])))
                self.ui.the2_current.setText(str(Userfunctions.convert_to_Deg(theta_flex[1])))
                self.ui.the3_current.setText(str(Userfunctions.convert_to_Deg(theta_flex[2])))
                T01 = self.Robot.initial_parameters(theta_flex,1)
                T02 = self.Robot.initial_parameters(theta_flex,2)
                T03 = self.Robot.initial_parameters(theta_flex,3)
                T0E = self.Robot.initial_parameters(theta_flex,4)
                x = np.array([T01[0,3],T02[0,3],T03[0,3],T0E[0,3]])
                y = np.array([T01[1,3],T02[1,3],T03[1,3],T0E[1,3]])
                z = np.array([T01[2,3],T02[2,3],T03[2,3],T0E[2,3]])
                self.screen.axes.clear()
                self.screen.config_display(self.screen)
                # line -[link length] plot
                self.screen.axes.plot([0,x[0]],[0,y[0]],[0,z[0]],linewidth=9)
                self.screen.axes.plot([x[0],x[1]],[y[0],y[1]],[z[0],z[1]],linewidth=9)
                self.screen.axes.plot([x[1],x[2]],[y[1],y[2]],[z[1],z[2]],linewidth=9)
                self.screen.axes.plot([x[2],x[3]],[y[2],y[3]],[z[2],z[3]],linewidth=9)
                # Joints syntaxis plot
                self.screen.axes.scatter(0, 0, 0, marker="o", color='k',s=200)
                self.screen.axes.scatter(x[0], y[0], z[0], marker="o", color='k',s=200)
                self.screen.axes.scatter(x[1], y[1], z[1], marker="o", color='k',s=200)
                self.screen.axes.scatter(x[2], y[2], z[2], marker="o", color='k',s=200)
                self.screen.axes.scatter(x[3], y[3], z[3], marker="o", color='k',s=200)
                self.screen.draw()
                self.ui.current_x.setText(str(np.round(x[3],2)))
                self.ui.current_y.setText(str(np.round(y[3],2)))
                self.ui.current_z.setText(str(np.round(z[3],2)))
                self.the1_current.setText(str(round(self.the1_flex,3)))
                self.the2_current.setText(str(round(self.the2_flex,3)))
                self.the3_current.setText(str(round(self.the3_flex,3)))

                self.the1pre = self.the1_flex
                self.the2pre = self.the2_flex
                self.the3pre = self.the3_flex
                self.idx += 1
            except:
                pass
class Worker(QtCore.QRunnable):

	def __init__(self, function, *args, **kwargs):
		super(Worker, self).__init__()
		self.function = function
		self.args = args
		self.kwargs = kwargs

	@pyqtSlot()
	def run(self):

		self.function(*self.args, **self.kwargs)


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
