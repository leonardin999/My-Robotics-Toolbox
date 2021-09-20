# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:20:12 2021

@author: Leonard
"""

from Libs.Planar_2dof_Libs import *
length_of_link = np.array([5,2])
Robot = Planar_2_DOF(length_of_link)
x,y,z = Robot.Inverse_kinematics(3,3,0,2)
Robot.Geometry_plot(x,y,z)