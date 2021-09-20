# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 22:20:45 2021

@author: Leonard
"""
from Robotics import *
import sympy as sym
alpha=[]
a=[]
d=[]
thelta=[]
print('Testing Robotics toolbox Function:')
n_dof=int(input('Please enter number Degree of Fredom: '))
#def __init__(self,n,alpha,a,d,thelta):
if n_dof<2 and n_dof>8:
    print('Number of Freedom out of range. Try again')
else:
    for i in range(n_dof):
        print('Enter Variables of Frame {}'.format(i+1))
        alp 	 = input('Link twist: ')
        offset   = input('Link offset: ')
        link_len = input('Link length: ')
        the 	 = input('joint angle (sym:the*): ')
        alpha.append(alp)
        a.append(offset)
        d.append(link_len)
        thelta.append(the)
    robot = ToolBox(n_dof,alpha,a,d,thelta)
    print(robot)
    T01 = robot.Transformation_matrix_symbolics(1)
    T02 = robot.Transformation_matrix_symbolics(2)
    print(T02)