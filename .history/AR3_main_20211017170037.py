# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 20:01:07 2021

@author: Leonard
"""
import numpy as np
import sys
from Libs.AR3_Libs import *
length = np.array([6.5,2.87,25.5,1.8,7.2,17.7,0,6.5])
Robot = AR3(length)
from threading import Thread
print(Robot)
opt = int(input('Choosing Option: ').strip())
if opt ==1:
    thelta = []
    print('Enter the value of joints angle:\n')
    for i in range (6):
        value = float(input('Theta{}: '.format(i+1)))
        thelta.append(value)
    Robot.Fkinematics(thelta,True)
    Robot.Drawing(thelta)
    
elif opt ==2:
    ## Examinate the Inverse Kinematics:
    print('Enter the value of End-effector position [x,y,z]: ')
    position = list(map(float,input('input: ').split(',')))
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
    thelta = [time]
    print('Enter the value of joints angle:\n')
    for i in range (6):
        value = float(input('Theta{}: '.format(i+1)))
        thelta.append(value)
    Robot.sending(thelta)
    Robot.recieving()

elif opt ==5:
    target=Robot.Reset_connection()

elif opt ==6:
    print('Enter the center position of circle [x,y,z]: ')
    center = list(map(float,input('input: ').split(',')))
    center = np.matrix(center).T
    radius = int(input('radius value in (cm): '))
    target=Robot.circle_drawing(radius,center)
else:
    print('try again!')
    pass