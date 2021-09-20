# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 08:11:38 2021

@author: Leonard
"""

import numpy as np
import math  as m
import sympy as sym
import matplotlib.pyplot as plt
from matplotlib import style

c = lambda x: np.cos(x)
s = lambda x: np.sin(x)
t = lambda x,y: m.atan2(x,y)

class Magician:
    def __init__(self,link_length):
        self.l = link_length
    def DHmatrix(self,alp,a,d,the):
        '''
        the is called the joint variable
        d is the joint variable
        The geometry of a robotic mechanism is conveniently defined 
        by attaching coordinate frames to each link.While these frames 
        could be located arbitrarily, it is advantageous both for 
        consistency and computational efficiency to 
        adhere to a convention for locating the frameson the links.
        '''
        Mdh=np.matrix([[c(the)        , -s(the)       , 0       , a],
                       [s(the)*c(alp) , c(the)*c(alp) ,-s(alp)  ,-d*s(alp)],
                       [s(the)*s(alp) , c(the)*s(alp) , c(alp)  , d*c(alp)],
                       [0             ,      0        , 0       , 1]])
        return Mdh
    
    def initial_parameters(self,the,option = 1):
        '''
        DHMATRIX Summary of this function goes here
         i      alpha(i-1)          di           a(i-1)        Thelta(i)
       joint    Link twist     Link Offset    Link Leight   Joint variable
         1       0                 0             L1             the1;...       %frame1
         2       pi/2              0             0              the2;...       %frame2
         3       0                 L2            0              the3;...       %frame3 
        end      0                 L3            0                0];          %End-point
        
         Joint frame with respect to the world coordinates.
        '''
        T01 = self.DHmatrix(0,self.l[0],0,the[0])
        T12 = self.DHmatrix(np.pi/2,0,0,the[1])
        T23 = self.DHmatrix(0,0,self.l[1],the[2])
        T3E = self.DHmatrix(0,0,self.l[2],0)
        # T01 = np.array([[c(the[0]), -s(the[0]), 0,          0],
        #                 [s(the[0]),  c(the[0]), 0,          0],
        #                 [0        ,          0, 1,  self.l[0]],
        #                 [0        ,          0, 0,          1]])
        
        # T12 = np.array([[c(the[1]), -s(the[1]),  0,  0],
        #                 [0        ,          0,  1,  0],
        #                 [s(the[1]),  c(the[1]),  0,  0],
        #                 [0        ,          0,  0,  1]])
        
        # T23 = np.array([[c(the[2]), -s(the[2]),  0,  self.l[1]],
        #                 [s(the[2]),  c(the[2]),  0,        0],
        #                 [0        ,          0,  1,        0],
        #                 [0        ,          0,  0,        1]])
        
        # T3E = np.array([[1,0, 0,  self.l[2]],
        #                 [0,1, 0,         0],
        #                 [0,0, 1,         0],
        #                 [0,0, 0,         1]])
        ## Tranformation Matrix:
        T02 = np.dot(T01,T12)
        T03 = np.dot(T02,T23)
        T0E = np.dot(T03,T3E)
        if   option == 1:
            return T01
        elif option == 2:
            return T02
        elif option == 3:
            return T03
        elif option == 4:
            return T0E
        
    def Forward_kinematis(self,the):
        End_Effector_Frame = self.initial_parameters(the,4)
        x = End_Effector_Frame[0,3]
        y = End_Effector_Frame[1,3]
        z = End_Effector_Frame[2,3]
        position = np.array([x,y,z])
        return position
    
    def Inverse_kinematics(self,pos,solution=1):
        #scenario 1:
        the1 = t(pos[1],pos[0])
        a1 = pos[2]-self.l[0]
        b1 = pos[0]/c(the1)
        p1 = (pos[0]/c(the1))**2 + (pos[2] - self.l[0])**2;
        cos_3 = (p1 - (self.l[1]*self.l[1]) - (self.l[2]*self.l[2]))/(2*self.l[1]*self.l[2]);
        r1 = self.l[1]+self.l[2]*cos_3
        the3 = np.array([t(np.sqrt(1-cos_3**2),cos_3),
                         t(-np.sqrt(1-cos_3**2),cos_3)])
        u1 =np.array([ a1 + np.sqrt( a1**2 + b1**2 - r1**2),
                       a1 - np.sqrt( a1**2 + b1**2 - r1**2)])
        k1 = r1 + b1
        the2 = np.array([2*t(u1[0],k1),
                         2*t(u1[1],k1)])
        #scenario 2:
        the1_1 = t(-pos[1],-pos[0])
        a = pos[2]-self.l[0]
        b = pos[0]/c(the1)
        p2 = (pos[0]/c(the1_1))**2 + (pos[2] - self.l[0])**2;
        cos1_3 = (p2 - (self.l[1]*self.l[1]) - (self.l[2]*self.l[2]))/(2*self.l[1]*self.l[2]);
        r = self.l[1]+self.l[2]*cos_3
        the3_1 = np.array([t(np.sqrt(1-cos1_3**2),cos1_3),
                         t(-np.sqrt(1-cos1_3**2),cos1_3)])
        u2 =np.array([ a + np.sqrt( a**2 + b**2 - r**2),
                       a - np.sqrt( a**2 + b**2 - r**2)])
        k2 = r + b
        the2_1 = np.array([2*t(u2[0],k2),
                         2*t(u2[1],k2)])
        if solution == 1:
            Sol1 = np.array([the1   ,  the2[0]  ,   the3[0]])
            return Sol1
        elif solution == 2:
            Sol2 = np.array([the1   ,  the2[0]  ,   the3[1]])
            return Sol2
        elif solution == 3:
            Sol3 = np.array([the1   ,  the2[1]  ,   the3[0]])
            return Sol3
        elif solution == 4:
            Sol4 = np.array([the1   ,  the2[1]  ,   the3[1]])
            return Sol4
        elif solution == 5:
            Sol5 = np.array([the1_1   ,  the2_1[0]  ,   the3_1[0]])
            return Sol5
        elif solution == 6:
            Sol6 = np.array([the1_1   ,  the2_1[0]  ,   the3_1[1]])
            return Sol6
        elif solution == 7:
            Sol7 = np.array([the1_1   ,  the2_1[1]  ,   the3_1[0]])
            return Sol7
        elif solution == 8:
            Sol8 = np.array([the1_1   ,  the2_1[1]  ,   the3_1[1]])
            return Sol8
    
    def geometry(self,the,title=" ",enable = False):
        T01 = self.initial_parameters(the,1)
        T02 = self.initial_parameters(the,2)
        T03 = self.initial_parameters(the,3)
        T0E = self.initial_parameters(the,4)
        x = np.array([T01[0,3],T02[0,3],T03[0,3],T0E[0,3]])
        y = np.array([T01[1,3],T02[1,3],T03[1,3],T0E[1,3]])
        z = np.array([T01[2,3],T02[2,3],T03[2,3],T0E[2,3]])
        plt.ion()
        plt.style.use("seaborn-notebook")
        fig = plt.figure()
        axis = fig.add_subplot(111,projection='3d') 
        
        # line -[link length] plot
        axis.plot([0,x[0]],[0,y[0]],[0,z[0]],linewidth=5)
        axis.plot([x[0],x[1]],[y[0],y[1]],[z[0],z[1]],linewidth=5)
        axis.plot([x[1],x[2]],[y[1],y[2]],[z[1],z[2]],linewidth=5)
        axis.plot([x[2],x[3]],[y[2],y[3]],[z[2],z[3]],linewidth=5)
        # Joints syntaxis plot
        axis.scatter(0, 0, 0, color='black',linewidth=8)
        axis.scatter(x[0], y[0], z[0], color='black',linewidth=7)
        axis.scatter(x[1], y[1], z[1], color='black',linewidth=7)
        axis.scatter(x[2], y[2], z[2], color='black',linewidth=7)
        axis.scatter(x[3], y[3], z[3], color='red',linewidth=7)
        if enable:
            label = '  ({:.1f},{:.1f},{:.1f})' .format(x[3], y[3],z[3])
            axis.text(x[3],y[3],z[3],label,fontsize=7,color='red')
        axis.set_xlim(-3, 8)
        axis.set_ylim(-3, 8)
        axis.set_zlim(-3, 8)
        axis.set_xlabel('X axis')
        axis.set_ylabel('Y axis')
        axis.set_zlabel('Z axis')
        plt.title(title)