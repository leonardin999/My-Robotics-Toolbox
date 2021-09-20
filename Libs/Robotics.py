# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:47:11 2021

@author: Leonard
"""
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
cosd = lambda x : np.cos( np.deg2rad(x))
sind = lambda x : np.sin( np.deg2rad(x))
c = lambda x : sym.cos(x)
s = lambda x : sym.sin(x)
class ToolBox:
    def __init__(self,n,alpha,a,d,thelta):
        self.link_twist  = alpha
        self.link_offset = a
        self.link_length = d
        self.joint_angle = thelta
        self.n  = n
    def __str__(self):
        line=""
        if not self.check_values():
            return "Invalid Input"
        else:
            line += "Ready to Using a Toolbox Functions for "+ str(self.n)+"-DOF"
            return line
    
    def check_values(self):
        if (len(self.link_length)== self.n 
            and len(self.link_twist)== self.n
            and len(self.link_offset)== self.n
            and len(self.joint_angle)== self.n):
            return True
        return False
    
    def DHmatrix(self,alpha,a,d,theta):
        Mdh=np.matrix([[cosd(theta)              , -sind(theta)             , 0             ,              a],
                       [sind(theta)*cosd(alpha)   , cosd(theta)*cosd(alpha)   , -sind(alpha)   ,  -d*sind(alpha)],
                       [sind(theta)*sind(alpha)   , cosd(theta)*sind(alpha)   , cosd(alpha)    ,   d*cosd(alpha)],
                       [0                 ,      0                  ,     0         ,              1]])
        return Mdh
    def DHmatrix_symbolics(self,alp,a,d,the):
        a = sym.Symbol(a)
        d = sym.Symbol(d)
        Mdh=np.matrix([[c(the)          ,-s(the)          , 0         ,          a],
                       [s(the)*c(alp)   , c(the)*c(alp)   , -s(alp)   ,  -d*s(alp)],
                       [s(the)*s(alp)   , c(the)*s(alp)   , c(alp)    ,   d*c(alp)],
                       [0               ,      0          ,     0     ,          1]])
        return Mdh
    
    def Transformation_matrix_symbolics(self,num_of_frame):
        if num_of_frame<1 and num_of_frame >self.n:
            print("Invalid Number of Frame")
        elif num_of_frame == 1:
            i = num_of_frame-1
            T = self.DHmatrix_symbolics(self.link_twist[i], self.link_offset[i],
                                        self.link_length[i], self.joint_angle[i])
            return np.matrix(sym.simplify(sym.Matrix(T)))
        else:
            T = np.eye(4,dtype=float)
            for i in range(num_of_frame):
                T_i = self.DHmatrix_symbolics(self.link_twist[i], self.link_offset[i],
                                              self.link_length[i], self.joint_angle[i])
                T = np.dot(T,T_i)
            return np.matrix(sym.simplify(sym.Matrix(T)))
        
    def Transformation_matrix(self,num_of_frame):
        if num_of_frame<1 and num_of_frame >self.n:
            print("Invalid Number of Frame")
        elif num_of_frame == 1:
            i = num_of_frame-1
            T = self.DHmatrix(self.link_twist[i], self.link_offset[i],
                              self.link_length[i], self.joint_angle[i])
            return np.matrix(T)
        else:
            T = np.eye(4,dtype=float)
            for i in range(num_of_frame):
                T_i = self.DHmatrix(self.link_twist[i], self.link_offset[i],
                              self.link_length[i], self.joint_angle[i])
                T = T*T_i
            return np.matrix(T)
    
    def end_point_position(self,x,y,z):
        Pos = np.transpose([x,y,z,1])
        T = self.Transformation_matrix_symbolics(self.n)
        return T*Pos
    
    def Jacobian(self):
        T=self.Transformation_matrix_symbolics(self.n)
        return T.jacobian(self.thelta)
    
    def Forward_Kinematics_2DOF(self):
        T01 = self.Transformation_matrix(1)
        T02 = self.Transformation_matrix(2)
        P1_ORG = np.matrix([0,0,0,1])
        P2_ORG = np.matrix([0,0,0,1])
        P01 = np.dot(T01,P1_ORG)
        P02 = np.dot(T02,P2_ORG)
        X = np.array([P01[0],P02[0]])
        Y = np.array([P01[1],P02[2]])
        Z = np.array([P01[2],P02[2]])
        return X,Y,Z
        
    def Forward_Kinematics_3DOF(self):
        T01 = self.Transformation_matrix(1)
        T02 = self.Transformation_matrix(2)
        T03 = self.Transformation_matrix(3)
        P1_ORG = np.matrix([0,0,0,1])
        P2_ORG = np.matrix([0,0,0,1])
        P3_ORG = np.matrix([0,0,0,1])
        P01 = np.dot(T01,P1_ORG)
        P02 = np.dot(T02,P2_ORG)
        P03 = np.dot(T03,P3_ORG)
        X = np.array([P01[0],P02[0],P03[0]])
        Y = np.array([P01[1],P02[1],P03[1]])
        Z = np.array([P01[2],P02[2],P03[2]])
        return X,Y,Z
    
    def Forward_Kinematics_4DOF(self):
        T01 = self.Transformation_matrix(1)
        T02 = self.Transformation_matrix(2)
        T03 = self.Transformation_matrix(3)
        T04 = self.Transformation_matrix(4)
        P1_ORG = np.matrix([0,0,0,1])
        P2_ORG = np.matrix([0,0,0,1])
        P3_ORG = np.matrix([0,0,0,1])
        P4_ORG = np.matrix([0,0,0,1])
        P01 = np.dot(T01,P1_ORG)
        P02 = np.dot(T02,P2_ORG)
        P03 = np.dot(T03,P3_ORG)
        P04 = np.dot(T03,P3_ORG)
        X = np.array([P01[0],P02[0],P03[0]])
        Y = np.array([P01[1],P02[1],P03[1]])
        Z = np.array([P01[2],P02[2],P03[2]])
        return X,Y,Z