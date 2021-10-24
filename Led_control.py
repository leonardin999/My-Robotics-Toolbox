# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 11:21:23 2021

@author: Leonard
"""



import numpy as np
from Libs.AR3_Libs import *
length = np.array([6.5,2.87,25.5,1.8,7.2,17.7,0,6.5])
Robot = AR3(length)
print('Basic LED contrller Program!\n')
Robot.Auto_connection()
time.sleep(1)
while True:
    theta = float(input('Value of Desired Angle: '))
    t_on  = int(input('Timming LED ON (milisecond): '))
    t_off = int(input('Timming LED OFF (milisecond): '))
    Robot.Led_Blink_send(theta, t_on, t_off)
    Robot.Led_Blink_recieve()
    if input('Run Again(Y/N)?').strip().upper()!='Y':
        Robot.Reset_connection()
        break
