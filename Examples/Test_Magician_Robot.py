# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 10:35:12 2021

@author: Leonard
"""

from Libs.Magician_Robotics_Libs import *
link_length = np.array([2,5,3])
#thelta = np.array([60,80,135])
position = np.array([4,3,1])
Robot = Magician(link_length)
thelta = Robot.Inverse_kinematics(position,4)
print(thelta)
Robot.geometry(thelta,"Geometry Presentation",True)