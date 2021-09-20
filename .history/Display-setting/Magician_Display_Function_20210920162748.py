from ui_styles import *

class UIFunctions():
    def toggleMenu_setting(self, maxWidth, enable):
        if enable:
            width = self.ui.frame_menu.width()
            maxExtend = maxWidth
            standard = 65

            if width == 65:
                self.ui.connection.show()
                self.ui.group_name.show()
                self.ui.simulation.show()
                widthExtended = maxExtend
            else:
                self.ui.connection.show()
                self.ui.group_name.show()
                self.ui.simulation.show()
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_menu, b"minimumWidth")
            self.animation.setStartValue(width)
            self.animation.setDuration(450)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def uiDefinitions(self):
        self.time_respond.setText('6 (s)')
        self.ui.mode_check.setChecked(False)
        self.btnstart_simu.setEnabled(False)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

        self.ui.widget.setGraphicsEffect(self.shadow)
        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 60))

        self.ui.frame_left_menu_3.setGraphicsEffect(self.shadow2)
        self.shadow3 = QGraphicsDropShadowEffect(self)
        self.shadow3.setBlurRadius(20)
        self.shadow3.setXOffset(0)
        self.shadow3.setYOffset(0)
        self.shadow3.setColor(QColor(0, 0, 0, 60))
        self.ui.btn_page_1.setGraphicsEffect(self.shadow3)

        self.shadow4 = QGraphicsDropShadowEffect(self)
        self.shadow4.setBlurRadius(20)
        self.shadow4.setXOffset(0)
        self.shadow4.setYOffset(0)
        self.shadow4.setColor(QColor(0, 0, 0, 60))
        self.ui.btn_page_2.setGraphicsEffect(self.shadow4)

        self.shadow5 = QGraphicsDropShadowEffect(self)
        self.shadow5.setBlurRadius(20)
        self.shadow5.setXOffset(0)
        self.shadow5.setYOffset(0)
        self.shadow5.setColor(QColor(0, 0, 0, 60))
        self.ui.btn_page_3.setGraphicsEffect(self.shadow5)

        self.shadow6 = QGraphicsDropShadowEffect(self)
        self.shadow6.setBlurRadius(20)
        self.shadow6.setXOffset(0)
        self.shadow6.setYOffset(0)
        self.shadow6.setColor(QColor(0, 0, 0, 60))
        self.ui.widget_2.setGraphicsEffect(self.shadow6)

        self.yaw_value.setText('0')
        self.pitch_value.setText('90')
        self.roll_value.setText('0')
        self.check_camera_4.setEnabled(False)
        self.check_arduino.setEnabled(False)
        self.check_rasp.setEnabled(False)
        self.check_camera.setEnabled(False)
        self.auto = False
        self.manual = False
