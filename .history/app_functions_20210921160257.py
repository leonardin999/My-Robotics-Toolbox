

import numpy as np
import math as m
import time
from Libs.Magician_Robotics_Libs import *
from Magician_main import *
class Userfunctions(MainWindow):
    def initialize_robot(self,length):
        self.Robot = Magician(length)
        if self.ui.the1_set.text()!="":
            self.the = [np.deg2rad(float(self.ui.the1_set.text())),
                        np.deg2rad(float(self.ui.the2_set.text())),
                        np.deg2rad(float(self.ui.the3_set.text())),
                        ]
    def convert_to_Deg(value):
        return np.round(np.rad2deg(value),2)
    def Geometry_display(self):
        try:
            self.the = [np.deg2rad(float(self.ui.the1_set.text())),
                        np.deg2rad(float(self.ui.the2_set.text())),
                        np.deg2rad(float(self.ui.the3_set.text())),
                        ]
            self.ui.the1_current.setText(str(Userfunctions.convert_to_Deg(self.the[0])))
            self.ui.the2_current.setText(str(Userfunctions.convert_to_Deg(self.the[1])))
            self.ui.the3_current.setText(str(Userfunctions.convert_to_Deg(self.the[2])))
            T01 = self.Robot.initial_parameters(self.the,1)
            T02 = self.Robot.initial_parameters(self.the,2)
            T03 = self.Robot.initial_parameters(self.the,3)
            T0E = self.Robot.initial_parameters(self.the,4)
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
            self.ui.current_x.setText(str(np.round(x[3],2)))
            self.ui.current_y.setText(str(np.round(y[3],2)))
            self.ui.current_z.setText(str(np.round(z[3],2)))
            self.screen.draw()
        except: print('loading....')
    def link_adjustment(self):
        self.link = [float(self.length1.text()),
                     float(self.length2.text()),
                     float(self.length3.text())]
        self.Robot.ChangeValue(self.link)
        Userfunctions.Geometry_display(self)

    def start_process(self):
        self.ui.idx=0
        self.the1pre = self.the2pre = self.the3pre = self.the4pre = self.the5pre =self.the6pre =0
        self.ui.the1_current.setText(str(self.the1pre))
        self.ui.the2_current.setText(str(self.the2pre))
        self.ui.the3_current.setText(str(self.the3pre))
        self.the = [np.deg2rad(float(self.ui.the1_current.text())),
                    np.deg2rad(float(self.ui.the2_current.text())),
                    np.deg2rad(float(self.ui.the3_current.text())),
                    ]
        position = self.Robot.Forward_kinematis(self.the)
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        self.stop_simulation_mode()
        self.start_simulation_mode()

    def Home_position(self):
            self.the1_set.setText('162')
            self.ui.the1_adjust.setValue(int(self.ui.the1_set.text()))
            self.the2_set.setText('23')
            self.ui.the2_adjust.setValue(int(self.ui.the2_set.text()))
            self.the3_set.setText('-75')
            self.ui.the3_adjust.setValue(int(self.ui.the3_set.text()))
            self.the = [np.deg2rad(float(self.ui.the1_set.text())),
                        np.deg2rad(float(self.ui.the2_set.text())),
                        np.deg2rad(float(self.ui.the3_set.text())),
                        ]
            if self.ui.mode_check.isChecked():
                Userfunctions.Trajectory(self.the)
            else:
                Userfunctions.Geometry_display(self)


    def forward_signal(self,step):
        x = int(self.ui.xpos.text())-step
        y = int(self.ui.ypos.text())
        z = int(self.ui.zpos.text())
        position =[x,y,z]
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        thelta = self.Robot.Inverse_kinematics(position,4)
        self.stop_simulation_mode()
        self.start_simulation_mode()

    def backward_signal(self,step):
        x = int(self.ui.xpos.text())+step
        y = int(self.ui.ypos.text())
        z = int(self.ui.zpos.text())
        position =[x,y,z]
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        thelta =self.Robot.Inverse_kinematics(position,4)
        self.stop_simulation_mode()
        self.start_simulation_mode()

    def left_signal(self,step):
        x = int(self.ui.xpos.text())
        y = int(self.ui.ypos.text())-step
        z = int(self.ui.zpos.text())
        position =[x,y,z]
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        thelta =self.Robot.Inverse_kinematics(position,4)
        self.stop_simulation_mode()
        self.start_simulation_mode()

    def right_signal(self,step):
        x = int(self.ui.xpos.text())
        y = int(self.ui.ypos.text())+step
        z = int(self.ui.zpos.text())
        position =[x,y,z]
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        thelta =self.Robot.Inverse_kinematics(position,4)
        self.stop_simulation_mode()
        self.start_simulation_mode()

    def up_signal(self,step):
        x = int(self.ui.xpos.text())
        y = int(self.ui.ypos.text())
        z = int(self.ui.zpos.text())+step
        position =[x,y,z]
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        thelta =self.Robot.Inverse_kinematics(position,4)
        self.stop_simulation_mode()
        self.start_simulation_mode()

    def down_signal(self,step):
        x = int(self.ui.xpos.text())
        y = int(self.ui.ypos.text())
        z = int(self.ui.zpos.text())-step
        position =[x,y,z]
        self.ui.xpos.setText(str(position[0]))
        self.ui.ypos.setText(str(position[1]))
        self.ui.zpos.setText(str(position[2]))
        thelta =self.Robot.Inverse_kinematics(position,4)
        self.stop_simulation_mode()
        self.start_simulation_mode()



