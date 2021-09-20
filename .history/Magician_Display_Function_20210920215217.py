from app_modules import *
from Magician_main import *
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
                self.ui.connection.hide()
                self.ui.group_name.hide()
                self.ui.simulation.hide()
                widthExtended = standard
            # ANIMATION
            self.animation = QPropertyAnimation(self.frame_menu, b"minimumWidth")
            self.animation.setStartValue(width)
            self.animation.setDuration(450)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def shadow_effect(self,widget):

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        widget.setGraphicsEffect(self.shadow)

    def uiDefinitions(self):
        self.ui.time_respond.setText('6 (s)')
        self.ui.mode_check.setChecked(False)
        self.ui.btn_start.setEnabled(False)
        self.ui.connection.hide()
        self.ui.group_name.hide()
        self.ui.simulation.hide()
        UIFunctions.shadow_effect(self,self.ui.Toggle_menu)
        UIFunctions.shadow_effect(self,self.ui.Universal_Display)
        UIFunctions.shadow_effect(self,self.ui.frame_time_adjust)
        UIFunctions.shadow_effect(self,self.ui.frame_current_DOF)
        UIFunctions.shadow_effect(self,self.ui.frame_current_pos)
        UIFunctions.shadow_effect(self,self.ui.frame_button)

    def valuechange(self):
        value_the1 = str(self.ui.the1_adjust.value())
        value_the2 = str(self.ui.the2_adjust.value())
        value_the3 = str(self.ui.the3_adjust.value())
        self.ui.the1_set.setText(value_the1)
        self.ui.the2_set.setText(value_the2)
        self.ui.the3_set.setText(value_the3)

    def timechange_plus(self):
        time = self.ui.time_respond.text().split()
        plus = int(time[0])+1
        if 0<plus and plus>20:
            self.ui.time_respond.setText(str(plus)+' (s)')
            self.ui.time_respond.adjustSize()
        else: pass

    def timechange_minus(self):
        time = self.ui.time_respond.text().split()
        minus = int(time[0])-1
        if 0<minus and minus>20:
            self.ui.time_respond.setText(str(minus)+' (s)')
            self.ui.time_respond.adjustSize()
        else: pass