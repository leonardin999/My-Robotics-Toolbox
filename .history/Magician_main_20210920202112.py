from PyQt5 import QtCore, QtGui, QtWidgets
from app_modules import *

class MainWindow(QMainWindow):
    def __init__(self):
        self.ui = uic.loadUi('Display_setting\Magician_Display.ui',self)
    #UIFunctions.uiDefinitions(self)
if __name__=="__main__":
    app = QGuiApplication(sys.argv)
    window = MainWindow()
    winow.show()
    sys.exit(app.exec_())
