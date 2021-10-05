# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:48:09 2021

@author: Leonard
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import matplotlib.animation as animation
from matplotlib import style
from Libs.AR3_Libs import *
length = np.array([6.5,2.87,25.5,1.8,7.2,17.7,0,6.5])
Robot = AR3(length)
t = np.linspace(0,10,100)
count = len(t)
center = np.matrix([-20.15 , 0 , 10.23]).T
radius = 10
theta = t*(2*np.pi/t[-1:])
points = center + radius*np.array([np.cos(theta), np.sin(theta),np.zeros(len(theta))])
Tx = points[0,:].T
Ty = points[1,:].T
Tz = points[2,:].T

plt.ion()
plt.style.use("seaborn-notebook")
fig = plt.figure()
axes = fig.add_subplot(111,projection='3d')  # set the axes for 3D plot

for i in range(len(Tx)):
    the = Robot.InverseKinematics(Tx[i],Ty[i],Tz[i])
    x,y,z = Robot.Fkinematics(the)
    axes.clear()
    axes.plot([0.0,x[0]],[0.0,y[0]],[-5,z[0]], linewidth=5)
    axes.plot([x[0],x[1]],[y[0],y[1]],[z[0],z[1]], linewidth=5)
    axes.plot([x[1],x[2]],[y[1],y[2]],[z[1],z[2]],linewidth=5)
    axes.plot([x[2],x[3]],[y[2],y[3]],[z[2],z[3]],linewidth=5)
    axes.plot([x[3],x[4]],[y[3],y[4]],[z[3],z[4]],linewidth=5)
    axes.plot([x[4],x[5]],[y[4],y[5]],[z[4],z[5]],linewidth=5,color='red')
    axes.plot([x[5],x[6]],[y[5],y[6]],[z[5],z[6]],linewidth=5)

    axes.scatter(0, 0, -5,color='k', marker="s",s=150)
    axes.scatter(x[0], y[0], z[0], marker="o", color='k',s=100)
    axes.scatter(x[1], y[1], z[1], marker="o", color='k',s=100)
    axes.scatter(x[2], y[2], z[2], marker="o", color='k',s=100)
    axes.scatter(x[3], y[3], z[3], marker="o", color='k',s=100)
    axes.scatter(x[4], y[4], z[4], marker="o", color='k',s=100)
    axes.scatter(x[5], y[5], z[5], marker="o", color='k',s=100)
    axes.scatter(x[6], y[6],z[6],s=100, marker="o",color='orange')

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
    plt.draw()
    plt.pause(0.01)
plt.cla()

plt.show(block=True)


