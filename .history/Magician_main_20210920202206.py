
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
        self.ui = uic.loadUi('Display_setting\Magician_Display.ui',self)
    UIFunctions.uiDefinitions(self)
if __name__=="__main__":
    app = QGuiApplication(sys.argv)
    window = MainWindow()
    winow.show()
    sys.exit(app.exec_())
