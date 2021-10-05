# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:42:33 2021

@author: Leonard
"""

import numpy as np
import math  as m
import sympy as sym
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
import serial.tools.list_ports
import serial
import time
import threading
warnings.filterwarnings('ignore')

c   = lambda x: np.cos(np.deg2rad(x))
s   = lambda x: np.sin(np.deg2rad(x))

class AR3:
    def __init__(self,link_length):
        self.d = link_length
        self.ser =  serial.Serial()
    
    def __str__(self):
        line = str('Operation option:\n1- Forward Kinematics\n2-Inverse Kinematics'+
      '\n3-Roll..Pitch..Yaw Examination\n4-Serial Connection\n5-Reset connection')
        return line
        
    def Fkinematics(self,thelta,allow = False):
        the1=thelta[0]; the2=thelta[1]; the3=thelta[2]; the4=thelta[3]; the5=thelta[4]; the6=thelta[5]
        T_01 = np.array([[c(the1) , -s(the1) , 0 , 0],
                          [s(the1) ,  c(the1) , 0 , 0],
                          [0     ,      0  ,  1 , 0],
                          [0     ,      0  ,  0 , 1]])
                   
        T_02 = np.array([[ c(the1)*c(the2),  -c(the1)*s(the2)  ,   s(the1)  , -self.d[1]*c(the1)],
                          [c(the2)*s(the1),  -s(the1)*s(the2)   , -c(the1)  , -self.d[1]*s(the1)],
                          [s(the2),              c(the2)     ,        0     ,           0],
                          [          0,                       0         ,    0        ,      1]])
                                 
        T_03 = np.array([[ c(the2 + the3)*c(the1)  ,  -s(the2 + the3)*c(the1)  ,   s(the1)  ,   -c(the1)*(self.d[1] - self.d[2]*c(the2))],
                          [ c(the2 + the3)*s(the1)  ,  -s(the2 + the3)*s(the1)  ,  -c(the1)  ,   -s(the1)*(self.d[1] - self.d[2]*c(the2))],
                          [ s(the2 + the3)        ,        c(the2 + the3)   ,          0        ,              self.d[2]*s(the2)],
                          [                   0         ,                      0         ,     0             ,                     1]])
        
        T_04 = np.array([[ -s(the1)*s(the4)-c(the4)*(c(the1)*s(the2)*s(the3) - c(the1)*c(the2)*c(the3))  ,      s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3))-c(the4)*s(the1)   ,    -s(the2 + the3)*c(the1)   ,     self.d[3]*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(self.d[4] + self.d[5]) - self.d[1]*c(the1)+self.d[2]*c(the1)*c(the2)],
                          [c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3) - c(the2)*c(the3)*s(the1))    ,     c(the1)*c(the4)+s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1))    ,   -s(the2 + the3)*s(the1)    ,    self.d[3]*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(self.d[4] + self.d[5]) - self.d[1]*s(the1)+self.d[2]*c(the2)*s(the1)],
                          [s(the2 + the3)*c(the4)                      ,                                                              -s(the2 + the3)*s(the4)           ,       c(the2 + the3)                               ,                      c(the2 + the3)*(self.d[4] + self.d[5]) + self.d[3]*s(the2+the3)+self.d[2]*s(the2)],
                          [0                                                       ,                                                         0           ,                      0               ,                                                                                                    1]])
         
          
        T_05 = np.array([[ -c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))    ,    s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))   ,    c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3))    ,      self.d[3]*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(self.d[4] + self.d[5])-self.d[1]*c(the1)+self.d[2]*c(the1)*c(the2)],
                          [c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))     ,   -s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))    ,    -c(the1)*c(the4)-s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1))   ,     self.d[3]*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(self.d[4] + self.d[5])-self.d[1]*s(the1)+self.d[2]*c(the2)*s(the1)],
                          [c(the2 + the3)*s(the5)+s(the2+the3)*c(the4)*c(the5)          ,                                                                                                                     c(the2+the3)*c(the5)-s(the2+the3)*c(the4)*s(the5)    ,                                                                           s(the2 + the3)*s(the4)              ,                                c(the2 + the3)*(self.d[4] + self.d[5]) + self.d[3]*s(the2 + the3)+self.d[2]*s(the2)],
                          [0                                                                                          ,                                                                                               0            ,                                                                                     0                                      ,                                                                     1]])
                          
        T_06 = np.array([[-s(the6)*(c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the6)*(c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))+s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)))  ,      s(the6)*(c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))+s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)))-c(the6)*(c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))    ,    s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))          ,       self.d[3]*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(self.d[4] + self.d[5])-self.d[1]*c(the1)+self.d[2]*c(the1)*c(the2)],
                          [s(the6)*(c(the1)*c(the4)+s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))+c(the6)*(c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)))   ,       c(the6)*(c(the1)*c(the4)+s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the6)*(c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)))   ,    -s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))         ,       self.d[3]*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(self.d[4] + self.d[5])-self.d[1]*s(the1)+self.d[2]*c(the2)*s(the1)],
                          [c(the6)*(c(the2 + the3)*s(the5)+s(the2 + the3)*c(the4)*c(the5))-s(the2 + the3)*s(the4)*s(the6)           ,                                                                                                                                                                                 -s(the6)*(c(the2 + the3)*s(the5)+s(the2 + the3)*c(the4)*c(the5))-s(the2 + the3)*c(the6)*s(the4)                               ,                                                                                                               c(the2 + the3)*c(the5)-s(the2 + the3)*c(the4)*s(the5)                        ,                                     c(the2 + the3)*(self.d[4] + self.d[5])+self.d[3]*s(the2 + the3)+self.d[2]*s(the2)],
                          [0                                                                                          ,                                                                                               0        ,                                                                                         0        ,                                                                                                   1]])
        P1_1org = np.array([0,0,0])
        P2_2org = np.array([0,0,0])
        P3_3org = np.array([0,0,0])
        P3_ee=    np.array([self.d[3],0,0])
        P4_4org = np.array([0,0,-self.d[5]])
        P5_5org = np.array([0,0,0])
        P6_ee = np.array([0,0,self.d[6]+self.d[7]])
        P_0_1_EX = np.dot(T_01,np.append(P1_1org,1))
        P_0_2_EX = np.dot(T_02,np.append(P2_2org,1))
        P_0_3_EX = np.dot(T_03,np.append(P3_3org,1))
        P_0_3ee  = np.dot(T_03,np.append(P3_ee,1))
        P_0_4_EX = np.dot(T_04,np.append(P4_4org,1))
        P_0_5_EX = np.dot(T_05,np.append(P5_5org,1))
        P_0_6_EX = np.dot(T_06,np.append(P6_ee,1))
        X=np.array([P_0_1_EX[0],P_0_2_EX[0],P_0_3_EX[0],P_0_3ee[0],P_0_4_EX[0],P_0_5_EX[0],P_0_6_EX[0]])
        Y=np.array([P_0_1_EX[1],P_0_2_EX[1],P_0_3_EX[1],P_0_3ee[1], P_0_4_EX[1],P_0_5_EX[1],P_0_6_EX[1]])
        Z=np.array([P_0_1_EX[2],P_0_2_EX[2],P_0_3_EX[2],P_0_3ee[2], P_0_4_EX[2],P_0_5_EX[2],P_0_6_EX[2]])
        if allow:
            value = np.round_(P_0_6_EX,3)
            print('The desired position following up the chosen joint angle is: x={}\ny={}\nz={}\n'.format(*value))
        return X,Y,Z
    def InverseKinematics(self,Px,Py,Pz,allow = False):
        Pz = Pz + self.d[6]+self.d[7];
        r11=  -1 ;  r12= 0;  r13= 0   ;    
        r21= 0  ; r22=1;   r23=0   ;     
        r31=0 ;  r32= 0;  r33=-1 ;
        r41=0 ; r42=0 ;r43=0 ; r44=1;
        T1 =np.empty(10, dtype=object)
        T2 =np.empty(10, dtype=object)
        T3 =np.empty(10, dtype=object)
        T4 =np.empty(10, dtype=object)
        T5 =np.empty(10, dtype=object)
        T6 =np.empty(10, dtype=object)
        T1[0] = m.atan2(-Py,-Px)
        
        a3 = 2*self.d[2]*self.d[3]
        b3 = -2*(self.d[4]+self.d[5])*self.d[2]
        c3 = Px*Px + Py*Py + Pz*Pz + self.d[1]*self.d[1] + 2*Px*m.cos(T1[0])*self.d[1] + 2*Py*m.sin(T1[0])*self.d[1] - self.d[2]*self.d[2] - self.d[3]*self.d[3] -(self.d[4]+self.d[5])*(self.d[4]+self.d[5])
        m1 = m.sqrt(a3*a3+b3*b3-c3*c3)
        T3[0]= m.atan2(b3,a3) + m.atan2(m1,c3)
        the1 = np.rad2deg(T1[0])
        the3 = np.rad2deg(T3[0])
        
        a= self.d[2] -(self.d[4]+self.d[5])*s(the3) + self.d[3]*c(the3)
        b = self.d[3]*s(the3) + (self.d[4]+self.d[5])*c(the3)
        c0 = c(the1)*Px + s(the1)*Py + self.d[1]
        d = Pz;
        T2[0]= m.atan2(a*d-b*c0,a*c0+b*d);
        the2 = np.rad2deg(T2[0]);
        
        T_03 = np.matrix([[c(the2 + the3)*c(the1)  ,   -s(the2 + the3)*c(the1) ,    s(the1)   ,  -c(the1)*(self.d[1] - self.d[2]*c(the2))],
                           [c(the2 + the3)*s(the1)  ,   -s(the2 + the3)*s(the1) ,   -c(the1)   ,  -s(the1)*(self.d[1] - self.d[2]*c(the2))],
                           [s(the2 + the3)              ,    c(the2 + the3)             ,  0               ,       self.d[2]*s(the2)               ],
                           [                0               ,                0                  ,  0               ,                   1]])
        T_03_inv =np.linalg.inv(T_03)
        
        
        a5= T_03_inv[1,0]*r13+T_03_inv[1,1]*r23+T_03_inv[1,2]*r33+T_03_inv[1,3]*r43;
        T5[0]=m.atan2(m.sqrt(1-a5*a5),a5)
        the5 = np.rad2deg(T5[0])
        
        a4= (T_03_inv[2,0]*r13+T_03_inv[2,1]*r23+T_03_inv[2,2]*r33+T_03_inv[2,3]*r43)/s(the5)
        b4= -(T_03_inv[0,0]*r13+T_03_inv[0,1]*r23+T_03_inv[0,2]*r33+T_03_inv[0,3]*r43)/s(the5)
        T4[0]= m.atan2(a4,b4)
        the4= np.rad2deg(T4[0])
        
        T_05 =np.matrix( [[-c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))   ,     s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))   ,    c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3))       ,   self.d[3]*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(self.d[4] + self.d[5])-self.d[1]*c(the1)+self.d[2]*c(the1)*c(the2)],
                          [c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))   ,     -s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))   ,     -c(the1)*c(the4)-s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1))    ,    self.d[3]*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(self.d[4] + self.d[5])-self.d[1]*s(the1)+self.d[2]*c(the2)*s(the1)],
                          [c(the2 + the3)*s(the5)+s(the2+the3)*c(the4)*c(the5) ,                                                                                                                              c(the2+the3)*c(the5)-s(the2+the3)*c(the4)*s(the5)   ,                                                                            s(the2 + the3)*s(the4)                                   ,           c(the2 + the3)*(self.d[4] + self.d[5]) + self.d[3]*s(the2 + the3)+self.d[2]*s(the2)],
                          [0                                                                               ,                                                                                                          0       ,                                                                                          0        ,                                                                                                   1]])                                                                                                                                                                                                                                                                                                                   
                 
        T_05_inv = np.linalg.inv(T_05) 
        a6=T_05_inv[0,0]*r11+T_05_inv[0,1]*r21+T_05_inv[0,2]*r31+T_05_inv[0,3]*r41
        b6=-(T_05_inv[2,0]*r11+T_05_inv[2,1]*r21+T_05_inv[2,2]*r31+T_05_inv[2,3]*r41)
        T6[0]=m.atan2(b6,a6)
        the6= np.rad2deg(T6[0])
        sum2 = np.array([the1,the2,the3,
                         the4,the5,the6]) 
        if allow:
            value = np.round_(sum2,3)
            print('The desired angle for each joints are:\nthelta1: {}\nthelta2: {}'
                  '\nthelta3: {}\nthelta4: {}\nthelta5: {}\nthelta5: {}\n'.format(*value))
        return sum2
    def get_wrist_center(self,gripper_point, R0g, dg = 6.5):
        xu, yu, zu = gripper_point 
          
        nx, ny, nz = R0g[0, 2], R0g[1, 2], R0g[2, 2]
        xw = xu - dg * nx
        yw = yu - dg * ny
        zw = zu - dg * nz 
      
        return np.array([xw, yw, zw])
    def Roll_Pitch_Yaw(self,Px,Py,Pz,yaw = 0,pitch = 0,roll = 0,allow = False):
        Pz = Pz + self.d[6];
        R0u = np.matrix([[1.0*c(yaw)*c(pitch), -1.0*s(yaw)*c(roll) + s(pitch)*s(roll)*c(yaw), 1.0*s(yaw)*s(roll) + s(pitch)*c(yaw)*c(roll)],
                         [1.0*s(yaw)*c(pitch),  s(yaw)*s(pitch)*s(roll) + 1.0*c(yaw)*c(roll), s(yaw)*s(pitch)*c(roll) - 1.0*s(roll)*c(yaw)],
                         [          -1.0*s(pitch),                                     1.0*s(roll)*c(pitch),                                    1.0*c(pitch)*c(roll)]])
        #R0u = Rotation_matrix(roll,pitch,yaw)
        rot_mat_06 = np.matrix([[-1.0, 0, 0],
                                [0, 1.0,  0],
                                [0, 0, -1.0]])
    
        r0g = R0u*rot_mat_06
        r11 = r0g[0,0] ; r12= r0g[0,1] ; r13 = r0g[0,2];
        r21 = r0g[1,0] ; r22= r0g[1,1] ; r23 = r0g[1,2];     
        r31 = r0g[2,0] ; r32= r0g[2,1] ; r33 = r0g[2,2];
        r41=0 ; r42=0 ;r43=0 ; r44=1;

        gripper_point = Px,Py,Pz
        wrist_center = self.get_wrist_center(gripper_point, r0g, dg = self.d[7])
        T1 =np.empty(10, dtype=object)
        T2 =np.empty(10, dtype=object)
        T3 =np.empty(10, dtype=object)
        T4 =np.empty(10, dtype=object)
        T5 =np.empty(10, dtype=object)
        T6 =np.empty(10, dtype=object)
        T1[0] = m.atan2(-wrist_center[1],-wrist_center[0])
        a3 = 2*self.d[2]*self.d[3]
        b3 = -2*(self.d[4]+self.d[5])*self.d[2]
        c3 = wrist_center[0]*wrist_center[0] + wrist_center[1]*wrist_center[1] + wrist_center[2]*wrist_center[2] + self.d[1]*self.d[1] + 2*wrist_center[0]*m.cos(T1[0])*self.d[1] + 2*wrist_center[1]*m.sin(T1[0])*self.d[1] - self.d[2]*self.d[2] - self.d[3]*self.d[3] -(self.d[4]+self.d[5])*(self.d[4]+self.d[5])
        m1 = m.sqrt(a3*a3+b3*b3-c3*c3)
        T3[0]= m.atan2(b3,a3) + m.atan2(m1,c3)
        the1 = np.rad2deg(T1[0])
        the3 = np.rad2deg(T3[0])
        
        a= self.d[2] -(self.d[4]+self.d[5])*s(the3) + self.d[3]*c(the3)
        b = self.d[3]*s(the3) + (self.d[4]+self.d[5])*c(the3)
        c0 = c(the1)*wrist_center[0] + s(the1)*wrist_center[1] + self.d[1]
        d = wrist_center[2];
        T2[0]= m.atan2(a*d-b*c0,a*c0+b*d);
        the2 = np.rad2deg(T2[0]);
        
        T_03 = np.matrix([[c(the2 + the3)*c(the1)  ,   -s(the2 + the3)*c(the1) ,    s(the1)   ,  -c(the1)*(self.d[1] - self.d[2]*c(the2))],
                           [c(the2 + the3)*s(the1)  ,   -s(the2 + the3)*s(the1) ,   -c(the1)   ,  -s(the1)*(self.d[1] - self.d[2]*c(the2))],
                           [s(the2 + the3)              ,    c(the2 + the3)             ,  0               ,       self.d[2]*s(the2)               ],
                           [                0               ,                0                  ,  0               ,                   1]])
        T_03_inv =np.linalg.inv(T_03)
        
        
        a5= T_03_inv[1,0]*r13+T_03_inv[1,1]*r23+T_03_inv[1,2]*r33+T_03_inv[1,3]*r43;
        T5[0]=m.atan2(m.sqrt(1-a5*a5),a5)
        the5 = np.rad2deg(T5[0])
        
        a4= (T_03_inv[2,0]*r13+T_03_inv[2,1]*r23+T_03_inv[2,2]*r33+T_03_inv[2,3]*r43)/s(the5)
        b4= -(T_03_inv[0,0]*r13+T_03_inv[0,1]*r23+T_03_inv[0,2]*r33+T_03_inv[0,3]*r43)/s(the5)
        T4[0]= m.atan2(a4,b4)
        the4= np.rad2deg(T4[0])
        
        T_05 =np.matrix( [[-c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))   ,     s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))   ,    c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3))       ,   self.d[3]*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(self.d[4] + self.d[5])-self.d[1]*c(the1)+self.d[2]*c(the1)*c(the2)],
                          [c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))   ,     -s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))   ,     -c(the1)*c(the4)-s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1))    ,    self.d[3]*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(self.d[4] + self.d[5])-self.d[1]*s(the1)+self.d[2]*c(the2)*s(the1)],
                          [c(the2 + the3)*s(the5)+s(the2+the3)*c(the4)*c(the5) ,                                                                                                                              c(the2+the3)*c(the5)-s(the2+the3)*c(the4)*s(the5)   ,                                                                            s(the2 + the3)*s(the4)                                   ,           c(the2 + the3)*(self.d[4] + self.d[5]) + self.d[3]*s(the2 + the3)+self.d[2]*s(the2)],
                          [0                                                                               ,                                                                                                          0       ,                                                                                          0        ,                                                                                                   1]])                                                                                                                                                                                                                                                                                                                   
                 
        T_05_inv = np.linalg.inv(T_05) 
        a6=T_05_inv[0,0]*r11+T_05_inv[0,1]*r21+T_05_inv[0,2]*r31+T_05_inv[0,3]*r41
        b6=-(T_05_inv[2,0]*r11+T_05_inv[2,1]*r21+T_05_inv[2,2]*r31+T_05_inv[2,3]*r41)
        T6[0]=m.atan2(b6,a6)
        the6= np.rad2deg(T6[0])
        sum2 = np.array([the1,the2,the3,
                         the4,the5,the6]) 
        if allow:
            value = np.round_(sum2,3)
            print('The desired angle for each joints are:\nthelta1: {}\nthelta2: {}'
                  '\nthelta3: {}\nthelta4: {}\nthelta5: {}\nthelta5: {}\n'.format(*value))
        return sum2
    def Drawing(self,thelta,allow = False):

        plt.style.use("seaborn-notebook")
        fig = plt.figure()
        fig.tight_layout()
        axes = fig.add_subplot(111,projection='3d')
        #axes.clear()
        x,y,z = self.Fkinematics(thelta,allow = False)
        axes.plot([0.0,x[0]],[0.0,y[0]],[-self.d[0],z[0]], linewidth=5)
        axes.plot([x[0],x[1]],[y[0],y[1]],[z[0],z[1]], linewidth=5)
        axes.plot([x[1],x[2]],[y[1],y[2]],[z[1],z[2]],linewidth=5)
        axes.plot([x[2],x[3]],[y[2],y[3]],[z[2],z[3]],linewidth=5)
        axes.plot([x[3],x[4]],[y[3],y[4]],[z[3],z[4]],linewidth=5)
        axes.plot([x[4],x[5]],[y[4],y[5]],[z[4],z[5]],linewidth=5,color='red')
        axes.plot([x[5],x[6]],[y[5],y[6]],[z[5],z[6]],linewidth=5)
    
        axes.scatter(0, 0, -self.d[0],color='k', marker="s",s=150)
        axes.scatter(x[0], y[0], z[0], marker="o", color='k',s=100)
        axes.scatter(x[1], y[1], z[1], marker="o", color='k',s=100)
        axes.scatter(x[2], y[2], z[2], marker="o", color='k',s=100)
        axes.scatter(x[3], y[3], z[3], marker="o", color='k',s=100)
        axes.scatter(x[4], y[4], z[4], marker="o", color='k',s=100)
        axes.scatter(x[5], y[5], z[5], marker="o", color='k',s=100)
        axes.scatter(x[6], y[6],z[6],s=100, marker="o",color='orange')
        if allow:
            label = '  ({:.1f},{:.1f},{:.1f})' .format(x[6], y[6],z[6])
            axes.text(x[6],y[6],z[6],label,fontsize=7,color='red')
        axes.set_xlim(10,-45)
        axes.set_ylim(-45, 35)
        axes.set_zlim(-5, 35)
        axes.set_xlabel('X_axis',color='k',fontsize=10)
        axes.set_ylabel('Y_axis',color='k',fontsize=10)
        axes.set_zlabel('Z_axis',color='k',fontsize=10)
        axes.tick_params(axis='x', colors='k')
        axes.tick_params(axis='y', colors='k')
        axes.tick_params(axis='z', colors='k')
        plt.title('AR3 Simulation Flatform')

    def Serial_connect(self,comm):
        self.ser.port = comm
        self.ser.baudrate =  115200
        self.ser.bytesize = serial.EIGHTBITS #number of bits per bytes
        self.ser.parity = serial.PARITY_NONE #set parity check: no parity
        self.ser.stopbits = serial.STOPBITS_ONE #number of stop bits            #timeout block read
        self.ser.xonxoff = False     #disable software flow control
        self.ser.rtscts = False     #disable hardware (RTS/CTS) flow control
        self.ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
        self.ser.writeTimeout = 0    #timeout for write
        self.ser.timeout =0
        self.ser.open()
        
    def Auto_connection(self):
        ports = serial.tools.list_ports.comports()
        self.commPort =([comport.device for comport in serial.tools.list_ports.comports()])
        self.numConnection = len(self.commPort)
        print('number of connection: {}'.format(self.numConnection))
        #self.Serial_connect(str(self.commPort[0]))
        self.ser = serial.Serial(self.commPort[0], baudrate=115200, timeout=1)

        
    def Reset_connection(self):
        if self.ser.isOpen():
            self.ser.close()
            
    def sending(self,theta):
        if self.ser.isOpen() and len(theta)>3:
            self.ser.write('{},{},{},{},{},{},{}'.format(*theta).encode())
            Data_send =str('{},{},{},{},{},{},{}'.format(*theta))
            #self.ser.flushInput()  #flush input buffer, discarding all its contents
            #self.ser.flushOutput()
            print(Data_send)

            
    def recieving(self):
        message=''
        with  open('data.txt', 'w') as output:
            while  self.ser.isOpen():
                strdata = self.ser.readline().decode()

                thelta = strdata.strip('\r\n').split(' ')
                if len(thelta) == 6:
                    message=strdata.strip('\r\n')+'\n'
                    output.write(message)
                    the = [float(thelta[0]),float(thelta[1]),float(thelta[2]),float(thelta[3]),float(thelta[4]),float(thelta[5])]
                    x,y,z = self.Fkinematics(the,allow = True)



