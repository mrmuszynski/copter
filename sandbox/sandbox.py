#! /usr/bin/env python3
###############################################################################
#
#	Title   : main.py
#	Author  : Matt Muszynski
#	Date    : 01/30/18
#	Synopsis: Sandbox script for copter
#
###############################################################################

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
import pdb
from numpy import array, sin, cos, vstack, empty, pi, arcsin, arccos
from numpy import rad2deg, deg2rad, ceil, cross, linspace, hstack
from numpy.linalg import norm

X = empty((0,3),float)
XDotHat = empty((0,3),float)
EAngles = empty((0,3),float)
x = array([0,0,0])



#b10 = n1
#b20 = n2
#b3 == xDotHat
class copter():
	def __init__(self):
		self.x = -1
		self.xDot = -1
		self.X = empty((0,3),float)
		self.XDot = empty((0,3),float)
		self.XDotHat = empty((0,3),float)
		self.EAngles = empty((0,3),float)
	def record(self):
		self.X = vstack([self.X,self.x])

	def flyStraight(self,params):
		direction,distance = params
		delta = 0.01
		for i in range(0,int(distance/delta)):
			self.x += delta*direction
			self.record()

	def flyCircle(self,params):
		import pdb
		pdb.set_trace()
		direction,normal,radius,angle = params
		direction = direction/norm(direction)
		normal = normal/norm(normal)
		delta = 0.01
		arclength = 2*pi*angle*radius/360
		nPoints = int(ceil(arclength/delta))
		#create arc in xy plane, centered on origin.
		DCM = vstack([
			-cross(direction,normal),
			direction,
			normal
			]).T
		newPoints = empty((0,3),float)
		theta = deg2rad(linspace(0,angle,nPoints+1))
		x = vstack([
			radius - radius*cos(theta),
			radius*sin(theta),
			theta-theta])
		x = DCM.dot(x)
		#shift start of curved path to current position
		self.X = vstack([self.X,x.T+self.x])
		self.x = self.X[-1]
	def runCommands(self):
		for func, param in zip(explorer.commands,explorer.cmdParam): 
			func(param)

explorer = copter()
explorer.commands = [
	explorer.flyStraight,
	explorer.flyStraight,
	explorer.flyStraight,
	explorer.flyCircle,
	explorer.flyCircle
]
explorer.cmdParam = [
	(array([1,0,0]),5),
	(array([0,1,0]),5),
	(array([0,0,1]),5),
	(array([0,0,1]),array([1,0,0]),5,180),
	(array([-1,0,1]),array([-1,0,-1]),5,180)
]
explorer.x = array([5.,5.,0.])
explorer.runCommands()


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(explorer.X[:,0], explorer.X[:,1], explorer.X[:,2], color='black')
# ax.auto_scale_xyz([-5, 5], [-5, 5], [0, 10])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')





# fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(X[:,0], X[:,1], X[:,2], color='black')
# ax.auto_scale_xyz([-5, 5], [-5, 5], [0, 10])
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# plt.figure()
# plt.plot(XDotHat)
# plt.figure()
# plt.plot(EAngles)
# plt.show()


pdb.set_trace()