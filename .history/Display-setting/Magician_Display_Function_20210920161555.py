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
