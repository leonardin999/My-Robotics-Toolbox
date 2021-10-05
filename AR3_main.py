# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:01:07 2021

@author: Leonard
"""
import numpy as np
from Libs.AR3_Libs import *
length = np.array([6.5,2.87,25.5,1.8,7.2,17.7,0,6.5])
Robot = AR3(length)
from threading import Thread
print(Robot)
opt = int(input('Choosing Option: ').strip())
if opt ==1:
    ## Examinate the Forward Kinematics:
    thelta = [0,90,0,0,90,0]
    Robot.Fkinematics(thelta,False)
    Robot.Drawing(thelta)
elif opt ==2:
    ## Examinate the Inverse Kinematics:
    position = [-27.8,0.0,20.8]
    Thelta = Robot.InverseKinematics(position[0],position[1],position[2],True)
    Robot.Drawing(Thelta,True)
elif opt ==3:
    ## Examinate the Roll Pitch Yaw in Robotics:
    position = [-27.8,0.0,20.8]
    roll = 30;pitch = 0; yaw = 40
    Thelta = Robot.Roll_Pitch_Yaw(position[0],position[1],position[2],roll,pitch,yaw,True)
    Robot.Drawing(Thelta,True)

elif opt ==4:
    ## Examinate cnnection by serial:
    Robot.Auto_connection()
    time.sleep(1)
    time = 4 ## in second
    data = [0,90,0,56,90,0,4]
    Robot.sending(data)
    Robot.recieving()

elif opt ==5:
    target=Robot.Reset_connection()
else:
    print('try again!')
    pass