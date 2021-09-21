
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
        UIFunctions.shadow_effect(self,self.ui.btn_plus)
        UIFunctions.shadow_effect(self,self.ui.btn_minus)
        UIFunctions.shadow_effect(self,self.ui.btn_home)
        UIFunctions.shadow_effect(self,self.ui.btn_reset)
        # initialize parameter:
        self.length1.setText('20')
        self.length2.setText('25')
        self.length3.setText('10')
        UIFunctions.Update_value(self)

        self.ui.mode_check.setChecked(False)

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
        if 0<plus and plus<20:
            self.ui.time_respond.setText(str(plus)+' (s)')
        else: pass

    def timechange_minus(self):
        time = self.ui.time_respond.text().split()
        minus = int(time[0])-1
        if 0<minus and minus<20:
            self.ui.time_respond.setText(str(minus)+' (s)')
        else: pass

    def length_change(self):
        self.ui.length1.setText('50')
        self.ui.length2.setText('40')
        self.ui.length3.setText('30')
        self.link = [float(self.length1.text()),
                        float(self.length2.text()),
                        float(self.length3.text())]
    def Update_value(self):
       self.ui.the1_adjust.setValue(int(self.ui.the1_set.text()))
       self.ui.the2_adjust.setValue(int(self.ui.the2_set.text()))
       self.ui.the3_adjust.setValue(int(self.ui.the3_set.text()))

    def reset(self):
        self.ui.the1_current.clear()
        self.ui.the2_current.clear()
        self.ui.the3_current.clear()

        self.ui.the1_set.clear()
        self.ui.the2_set.clear()
        self.ui.the3_set.clear()

        self.ui.length1.clear()
        self.ui.length2.clear()
        self.ui.length3.clear()

        self.ui.the1_adjust.setValue(0)
        self.ui.the2_adjust.setValue(0)
        self.ui.the3_adjust.setValue(0)

        self.ui.xpos.clear()
        self.ui.ypos.clear()
        self.ui.zpos.clear()

        self.ui.mode_check.setChecked(False)
    def simulation_check(self):
        if self.ui.mode_check.isChecked():
            self.btn_start.setEnabled(True)
        else:
            self.btn_start.setEnabled(False)
