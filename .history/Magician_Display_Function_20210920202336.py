from app_modules import *
class UIFunctions(MainWindow):
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

    def shadow_effect(self,widget):
        widget.setGraphicsEffect(self.shadow)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))

    def uiDefinitions(self):
        self.time_respond.setText('6 (s)')
        self.ui.mode_check.setChecked(False)
        self.ui.btn_start.setEnabled(False)

        UIFunctions.shadow_effect(self.ui.Toggle_menu)
        UIFunctions.shadow_effect(self.ui.Universal_Display)
        UIFunctions.shadow_effect(self.ui.frame_time_adjust)
        UIFunctions.shadow_effect(self.ui.frame_current_DOF)
        UIFunctions.shadow_effect(self.ui.frame_current_pos)
        UIFunctions.shadow_effect(self.ui.frame_button)
