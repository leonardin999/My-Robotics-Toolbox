# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:38:22 2021

@author: Leonard
"""

import numpy as np
import math as m
import sympy as sympy
import matplotlib.pyplot as plt
from matplotlib import style
# Creating a Shortcut syntaxis#
c = lambda x: np.cos(np.deg2rad(x))
s = lambda x: np.sin(np.deg2rad(x))

# initialize a 2-DOF planar Library #

class Planar_2_DOF:
    def __init__(self,link_length):
        '''
        Create a Planar 2 DOF robotics arm for simulation

        Parameters
        ----------
        link_length : A 2D array that list a length of each link
        '''
        self.length = link_length

    def Forward_kinematic(self,theta1,theta2):
        P01 = np.array([self.length[0]*c(theta1),self.length[0]*s(theta1),0])

        P02 = np.array([self.length[0]*c(theta1)+self.length[1]*c(theta1+theta2),
                        self.length[0]*s(theta1)+self.length[1]*s(theta1+theta2),
                        0])
        x = np.array([P01[0],P02[0]])
        y = np.array([P01[1],P02[1]])
        z = np.array([P01[2],P02[2]])
        return x,y,z
    def endpoint_position(self,theta1,theta2):
        x,y,z = self.Forward_kinematic(theta1,theta2)
        position = np.array([x[1],y[1],z[1]])
        return position
    def Geometry_plot(self,x,y,z):
        plt.ion()
        plt.style.use("seaborn-notebook")
        fig = plt.figure()
        axis = fig.add_subplot(111,projection='3d') 
        # line -[link length] plot
        axis.plot([0,0],[0,0],[-5,0],linewidth=5)
        axis.plot([0,x[0]],[0,y[0]],[0,z[0]],linewidth=5)
        axis.plot([x[0],x[1]],[y[0],y[1]],[z[0],z[1]],linewidth=5)
        # Joints syntaxis plot
        axis.scatter(0, 0, -5, color='black',linewidth=10)
        axis.scatter(0, 0, 0, color='black',linewidth=10)
        axis.scatter(x[0], y[0], z[0], color='black',linewidth=10)
        axis.scatter(x[1], y[1], z[1], color='red',linewidth=10)
        label = '  ({:.1f},{:.1f},{:.1f})' .format(x[1], y[1],z[1])
        axis.text(x[1],y[1],z[1],label,fontsize=7,color='black')
        axis.set_xlim(-5, 5)
        axis.set_ylim(-5, 5)
        axis.set_zlim(-10, 20)
        axis.set_xlabel('X axis')
        axis.set_ylabel('Y axis')
        axis.set_zlabel('Z axis')
        plt.title('2 DOF Simulation')
        
    def Inverse_kinematics(self,x,y,z,solution =1):
        a = x^2 + y^2 - (self.length[0])^2 - (self.length[1])^2
        b = 2*(self.length[0])*(self.length[1])
        c2 = a/b
        s2 = np.sqrt(1-c2**2)
        theta2 = np.array([m.atan2(s2,c2),m.atan2(-s2,c2)])
        theta1 = np.array([m.atan2(y, x) -m.atan2(self.length[1]*s(theta2[0]), self.length[0]+self.length[1]*c(theta2[0])),
                           m.atan2(y, x) -m.atan2(self.length[1]*s(theta2[1]), self.length[0]+self.length[1]*c(theta2[1]))])
        if solution == 1:
            x,y,z = self.Forward_kinematic(theta1[0],theta2[1])
        elif solution ==2:
            x,y,z = self.Forward_kinematic(theta1[1],theta2[0])
        
        return x,y,z