#! /usr/bin/env python3
###############################################################################
#
#	Title   : weaveTest.py
#	Author  : Matt Muszynski
#	Date    : 02/02/18
#	Synopsis: Playing with patterns
#
###############################################################################

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
import pdb
from numpy import array, sin, cos, vstack, empty, pi, arcsin, zeros
from numpy import rad2deg, deg2rad, ceil, cross, linspace, hstack, ones
from numpy.linalg import norm



def r3 (theta):
	r3 = array([
		[ cos(theta),sin(theta),0],
		[-sin(theta),cos(theta),0],
		[          0,         0,1]
		])
	return r3

n = 6
#theta is the angle for the sinusoid
theta = deg2rad(linspace(0,360*n,3600*n))
#twist controls how much the sinusoid rotates about its path
twist = deg2rad(linspace(0,360*n,3600*n))/n*2*0
#spin controls where the CoM
spin  = deg2rad(linspace(0,360*n,3600*n))

CoM = 10*vstack([cos(spin),sin(spin),zeros(3600*n)])

sinWave = sin(theta*25) 
cosWave = cos(theta*n)

sinWave3D = vstack([sinWave*sin(twist),zeros(len(sinWave)),sinWave*cos(twist)])
sinWave3D2 = vstack([sinWave*sin(pi/2),zeros(len(sinWave)),sinWave*cos(pi/2)])

totalMotion = CoM + sinWave3D
totalMotion2 = CoM + sinWave3D2

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(totalMotion[0],totalMotion[1],totalMotion[2], color='black')
ax.plot(totalMotion2[0],totalMotion2[1],totalMotion2[2], color='black')
ax.set_xlim([-10,10])
ax.set_ylim([-10,10])
ax.set_zlim([-10,10])
pdb.set_trace()