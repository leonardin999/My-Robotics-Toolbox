
import platform
import os
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
## import Matplotlib in Pyqt5
import matplotlib
from matplotlib import style
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as Canvas
from matplotlib.animation import FuncAnimation
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = uic.loadUi('Display_setting/Magician_Display.ui',self)
        #self.ui.setupUi(self)
        print('System: '+platform.system())
        print('Version: '+platform.release())
        self.ui.btn_Setting.clicked.connect(lambda: UIFunctions.toggleMenu_setting(self,280,True))
        UIFunctions.uiDefinitions(self)
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
