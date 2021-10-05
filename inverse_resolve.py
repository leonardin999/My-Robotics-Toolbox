# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 14:15:49 2021

@author: Leonard
"""

import numpy as np
import math  as m
import sympy as sym
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
warnings.warn('Ignore')

c   = lambda x: np.cos(np.deg2rad(x))
s   = lambda x: np.cos(np.deg2rad(x))
t   = lambda x,y: m.atan2(x,y)
inv = lambda A: np.linalg.inv(A)
d0 = 50; d1 = 28.7; d2 = 255; d3 = 18; d4 = 72; d5 = 177; d6=  0; d7= 65;
the1 =0
the2=90
the3=0
the4=0
the5=90
the6=0
T1=T2=T3=T4=T5=T6={}
T06 = np.matrix([[-s(the6)*(c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the6)*(c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))+s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2))),s(the6)*(c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))+s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)))-c(the6)*(c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3))),s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),d3*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(d4 + d5)-d1*c(the1)+d2*c(the1)*c(the2)],
                 [s(the6)*(c(the1)*c(the4)+s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))+c(the6)*(c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))),c(the6)*(c(the1)*c(the4)+s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the6)*(c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2))),-s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),d3*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(d4 + d5)-d1*s(the1)+d2*c(the2)*s(the1)],
                 [c(the6)*(c(the2 + the3)*s(the5)+s(the2 + the3)*c(the4)*c(the5))-s(the2 + the3)*s(the4)*s(the6),-s(the6)*(c(the2 + the3)*s(the5)+s(the2 + the3)*c(the4)*c(the5))-s(the2 + the3)*c(the6)*s(the4),c(the2 + the3)*c(the5)-s(the2 + the3)*c(the4)*s(the5),c(the2 + the3)*(d4 + d5)+d3*s(the2 + the3)+d2*s(the2)]])
                                                                                                                                                                                    
r11 = T06[0,0] ; r12= T06[0,1] ; r13 = T06[0,2];
r21 = T06[1,0] ; r22= T06[1,1] ; r23 = T06[1,2];     
r31 = T06[2,0] ; r32= T06[2,1] ; r33 = T06[2,2];
r41=0 ; r42=0 ;r43=0 ; r44=1;
Px=T06[0,3]
Py=T06[1,3]
Pz=T06[2,3]
T1[0,0] = t(-Py,-Px);

a3 = 2*d2*d3
b3 = -2*(d4+d5)*d2
c3 = Px*Px + Py*Py + Pz*Pz + d1*d1 + 2*Px*c(T1[0,0])*d1 + 2*Py*s(T1[0,0])*d1 - d2*d2 - d3*d3 -(d4+d5)*(d4+d5)
m = np.sqrt(a3*a3+b3*b3-c3*c3);
T3[0,0]= t(b3,a3) + t(m,c3)
the1 = T1[0,0]
the3 = T3[0,0]

a= d2 -(d4+d5)*s(the3) + d3*c(the3); 
b = d3*s(the3) + (d4+d5)*c(the3);
c = c(the1)*Px + s(the1)*Py + d1;
d = Pz;
T2[0,0]= t(a*d-b*c,a*c+b*d);
the2 = T2[0,0];

T03 = np.matrix([[c(the2 + the3)*c(the1),-s(the2 + the3)*c(the1),s(the1),-c(the1)*(d1 - d2*c(the2))],
                 [c(the2 + the3)*s(the1),-s(the2 + the3)*s(the1),-c(the1),-s(the1)*(d1 - d2*c(the2))],
                 [s(the2 + the3),c(the2 + the3),0,d2*s(the2)],
                 [0,0,0,1]])
T03_inv =inv(T03)

a5= T03_inv[1,0]*r13+T03_inv[1,1]*r23+T03_inv[1,2]*r33+T03_inv[1,3]*r43
T5[0,0]=t(np.sqrt(1-a5*a5),a5)
the5 = T5[0,0]

a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5)
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5))
the4= t(a4,b4)
T4[0,0]= the4

T05 = np.matrix([[-c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)),d3*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(d4 + d5)-d1*c(the1)+d2*c(the1)*c(the2)],
                 [c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),-s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),-c(the1)*c(the4)-s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)),d3*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(d4 + d5)-d1*s(the1)+d2*c(the2)*s(the1)],
                 [c(the2 + the3)*s(the5)+s(the2+the3)*c(the4)*c(the5),c(the2+the3)*c(the5)-s(the2+the3)*c(the4)*s(the5),s(the2 + the3)*s(the4),c(the2 + the3)*(d4 + d5) + d3*s(the2 + the3)+d2*s(the2)],
                 [0,0,0,1]])                                                                                                                                                                                                                                                                                                                   
                                                                                                         
T05_inv = inv(T05) 
a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41)
the6=t(b6,a6)
T6[0,0]= the6

T5[0,1]=t(-np.sqrt(1-a5*a5),a5)
the5 = T5[0,1]
a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5)
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5))
T4[0,1]=t(a4,b4)
the4 =T4[0,1]

T05 = np.matrix([[-c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)),d3*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(d4 + d5)-d1*c(the1)+d2*c(the1)*c(the2)],
                 [c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),-s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),-c(the1)*c(the4)-s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)),d3*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(d4 + d5)-d1*s(the1)+d2*c(the2)*s(the1)],
                 [c(the2 + the3)*s(the5)+s(the2+the3)*c(the4)*c(the5),c(the2+the3)*c(the5)-s(the2+the3)*c(the4)*s(the5),s(the2 + the3)*s(the4),c(the2 + the3)*(d4 + d5) + d3*s(the2 + the3)+d2*s(the2)],
                 [0,0,0,1]])                                                                                                                                                                                                                                                                                                                   
T05_inv=inv(T05)
a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41;
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41);
T6[0,1]=t(b6,a6)
the6 = T6[0,1]


T3[0,1]= t(b3,a3) + t(-m,c3);
the1 = T1[0,0];
the3 = T3[0,1];

a= d2 -(d4+d5)*s(the3) + d3*c(the3); 
b = d3*s(the3) + (d4+d5)*c(the3);
c = c(the1)*Px + s(the1)*Py + d1;
d = Pz;
T2[0,1]= t(a*d-b*c,a*c+b*d);
the2 = T2[0,1];

a5= T03_inv[1,0]*r13+T03_inv[1,1]*r23+T03_inv[1,2]*r33+T03_inv[1,3]*r43
T5[0,2]=t(np.sqrt(1-a5*a5),a5)
the5 = T5[0,2]

a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5);
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5));
the4= t(a4,b4);
T4[0,2]= the4;

T05 = np.matrix([[-c(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-s(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),s(the5)*(s(the1)*s(the4)+c(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)))-c(the5)*(c(the1)*c(the2)*s(the3)+c(the1)*c(the3)*s(the2)),c(the4)*s(the1)-s(the4)*(c(the1)*s(the2)*s(the3)-c(the1)*c(the2)*c(the3)),d3*c(the2 + the3)*c(the1)-s(the2 + the3)*c(the1)*(d4 + d5)-d1*c(the1)+d2*c(the1)*c(the2)],
                 [c(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-s(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),-s(the5)*(c(the1)*s(the4)-c(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)))-c(the5)*(c(the2)*s(the1)*s(the3)+c(the3)*s(the1)*s(the2)),-c(the1)*c(the4)-s(the4)*(s(the1)*s(the2)*s(the3)-c(the2)*c(the3)*s(the1)),d3*c(the2 + the3)*s(the1)-s(the2 + the3)*s(the1)*(d4 + d5)-d1*s(the1)+d2*c(the2)*s(the1)],
                 [c(the2 + the3)*s(the5)+s(the2+the3)*c(the4)*c(the5),c(the2+the3)*c(the5)-s(the2+the3)*c(the4)*s(the5),s(the2 + the3)*s(the4),c(the2 + the3)*(d4 + d5) + d3*s(the2 + the3)+d2*s(the2)],
                 [0,0,0,1]])                                                                                                                                                                                                                                                                                                                   
T05_inv=inv(T05)
a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41;
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41);
the6=t(b6,a6);
T6[0,2]= the6;

T5[0,3]=t(-np.sqrt(1-a5*a5),a5);
the5 = T5[0,3];
a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5);
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5));
T4[0,3]=t(a4,b4);
the4 =T4[0,3];

a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41;
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41);
T6[0,3]=t(b6,a6);
the6 = T6[0,3];

T1[0,1] = t(Py,Px);
the1 = T1[0,1];
a3 = 2*d2*d3;
b3 = -2*(d4+d5)*d2;
c3 = Px*Px + Py*Py + Pz*Pz + d1*d1 + 2*Px*c(T1[0,1])*d1 + 2*Py*s(T1[0,1])*d1 - d2*d2 - d3*d3 -(d4+d5)*(d4+d5);
m = np.sqrt(a3*a3+b3*b3-c3*c3);
T3[0,2]= t(b3,a3) + t(m,c3);

the3 = T3[0,2];

a= d2 -(d4+d5)*s(the3) + d3*c(the3); 
b = d3*s(the3) + (d4+d5)*c(the3);
c = c(the1)*Px + s(the1)*Py + d1;
d = Pz;
T2[0,2]= t(a*d-b*c,a*c+b*d);
the2 = T2[0,2];

a5= T03_inv[1,0]*r13+T03_inv[1,1]*r23+T03_inv[1,2]*r33+T03_inv[1,3]*r43;
T5[0,4]=t(np.sqrt(1-a5*a5),a5);
the5 = T5[0,4];

a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5);
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5));
the4= t(a4,b4);
T4[0,4]= the4;

a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41;
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41);
the6=t(b6,a6);
T6[0,4]= the6;

T5[0,5]=t(-np.sqrt(1-a5*a5),a5);
the5 = T5[0,5];
a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5);
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5));
T4[0,5]=t(a4,b4);
the4 =T4[0,5];

a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41;
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41);
T6[0,5]=t(b6,a6);
the6 = T6[0,5];

T3[0,3]= t(b3,a3) + t(-m,c3);
the1 = T1[0,1];
the3 = T3[0,3];

a= d2 -(d4+d5)*s(the3) + d3*c(the3); 
b = d3*s(the3) + (d4+d5)*c(the3);
c = c(the1)*Px + s(the1)*Py + d1;
d = Pz;
T2[0,3]= t(a*d-b*c,a*c+b*d);
the2 = T2[0,3];

a5= T03_inv[1,0]*r13+T03_inv[1,1]*r23+T03_inv[1,2]*r33+T03_inv[1,3]*r43;
T5[0,6]=t(np.sqrt(1-a5*a5),a5);
the5 = T5[0,6];

a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5);
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5));
the4= t(a4,b4);
T4[0,6]= the4;

a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41)
the6=t(b6,a6)
T6[0,6]= the6

T5[0,7]=t(-np.sqrt(1-a5*a5),a5)
the5 = T5[0,7]
a4= (T03_inv[2,0]*r13+T03_inv[2,1]*r23+T03_inv[2,2]*r33+T03_inv[2,3]*r43)/s(the5)
b4= -((T03_inv[0,0]*r13+T03_inv[0,1]*r23+T03_inv[0,2]*r33+T03_inv[0,3]*r43)/s(the5))
T4[0,7]=t(a4,b4)
the4 =T4[0,7]

a6=T05_inv[0,0]*r11+T05_inv[0,1]*r21+T05_inv[0,2]*r31+T05_inv[0,3]*r41;
b6=-(T05_inv[2,0]*r11+T05_inv[2,1]*r21+T05_inv[2,2]*r31+T05_inv[2,3]*r41);
T6[0,7]=t(b6,a6);
the6 = T6[0,7];

the1= np.array([T1[0,0],T1[0,0],T1[0,0],T1[0,0],T1[0,1],T1[0,1],T1[0,1],T1[0,1]])
the2= np.array([T2[0,0],T2[0,0],T2[0,1],T2[0,1],T2[0,2],T2[0,2],T2[0,3],T2[0,3]])
the3= np.array([T3[0,0],T3[0,0],T3[0,1],T3[0,1],T3[0,2],T3[0,2],T3[0,3],T3[0,3]])
the4= np.array([T4[0,0],T4[0,1],T4[0,2],T4[0,3],T4[0,4],T4[0,5],T4[0,6],T4[0,7]])
the5= np.array([T5[0,0],T5[0,1],T5[0,2],T5[0,3],T5[0,4],T5[0,5],T5[0,6],T5[0,7]])
the6= np.array([T6[0,0],T6[0,1],T6[0,2],T6[0,3],T6[0,4],T6[0,5],T6[0,6],T6[0,7]])
