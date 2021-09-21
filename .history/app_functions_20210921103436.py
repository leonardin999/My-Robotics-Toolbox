

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
    def Geometry_display(self):
        try:
            while self.ui.the1_set.text()!="":
                self.the = [np.deg2rad(float(self.ui.the1_set.text())),
                            np.deg2rad(float(self.ui.the2_set.text())),
                            np.deg2rad(float(self.ui.the3_set.text())),
                            ]
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
                self.screen.axes.plot([0,x[0]],[0,y[0]],[0,z[0]],linewidth=5)
                self.screen.axes.plot([x[0],x[1]],[y[0],y[1]],[z[0],z[1]],linewidth=5)
                self.screen.axes.plot([x[1],x[2]],[y[1],y[2]],[z[1],z[2]],linewidth=5)
                self.screen.axes.plot([x[2],x[3]],[y[2],y[3]],[z[2],z[3]],linewidth=5)
                # Joints syntaxis plot
                self.screen.axes.scatter(0, 0, 0, color='black',linewidth=8)
                self.screen.axes.scatter(x[0], y[0], z[0], color='black',linewidth=7)
                self.screen.axes.scatter(x[1], y[1], z[1], color='black',linewidth=7)
                self.screen.axes.scatter(x[2], y[2], z[2], color='black',linewidth=7)
                self.screen.axes.scatter(x[3], y[3], z[3], color='red',linewidth=7)
                self.screen.draw()
        except: pass