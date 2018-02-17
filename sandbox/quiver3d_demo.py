#! /usr/bin/env python3

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy import cos, sin, deg2rad, array,vstack,empty,pi, sqrt
from numpy import identity
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
import pdb

def r1(theta):
	r1 =  array( \
	[ \
	[1.,             0.,         0.    ], \
	[0.,   cos(theta), sin(theta)], \
	[0.,  -sin(theta), cos(theta)]  \
	] \
	)	
	return r1

def r2(theta):
	r2 =  array( \
	[ \
	[ cos(theta), 0., -sin(theta)], \
	[ 0.,         1., 0.         ], \
	[ sin(theta), 0., cos(theta)]  \
	] \
	)	
	return r2

def r3 (theta):
	r3 = array( \
	[ \
	[  cos(theta),    sin(theta), 0.], \
	[ -sin(theta),    cos(theta), 0.], \
	[ 0.,                0.,      1.]  \
	] \
	)
	return r3

def norm(vectorStack):
	return (
		vectorStack.T/sqrt(
			vectorStack[:,0]**2 + \
			vectorStack[:,1]**2 + \
			vectorStack[:,2]**2
			)
		).T

alpha = deg2rad(20)
beta = -deg2rad(10)
gamma = deg2rad(45)



n1Hat = array([ 0,1,0])
n2Hat = array([-1,0,0])
n3Hat = array([ 0,0,1])

No = array([5.,0.,0.]) #origin begins at [1,0,0]

fig = plt.figure()
ax = fig.gca(projection='3d')

wave1 = empty((0,3),float)
wave2 = empty((0,3),float)

for i in range(0,3600):
	theta = deg2rad(0.1)*i
	rotate = r3(-theta)
	twist1 = r2(deg2rad(45))
	twist2 = r2(deg2rad(-45))
	Co = rotate.dot(No)
	c1Hat = rotate.dot(twist1.dot(n1Hat))
	c2Hat = rotate.dot(twist1.dot(n2Hat))
	c3Hat = rotate.dot(twist1.dot(n3Hat))
	d3Hat = rotate.dot(twist2.dot(n3Hat))
	o1, o2, o3 = Co
	wave1 = vstack([wave1,Co + sin(10*theta)*c3Hat])
	wave2 = vstack([wave2,Co + sin(pi/2+10*theta)*d3Hat])
	# if i%360 == 0:
	# 	ax.quiver(o1, o2, o3,[c1Hat[0]],[c1Hat[1]],[c1Hat[2]],
	# 		length=1, normalize=True,color='green')
	# 	ax.quiver(o1, o2, o3,[c2Hat[0]],[c2Hat[1]],[c2Hat[2]],
	# 		length=1, normalize=True,color='red')
	# 	ax.quiver(o1, o2, o3,[c3Hat[0]],[c3Hat[1]],[c3Hat[2]],
	# 		length=1, normalize=True,color='blue')
plt.plot(wave1[:,0],wave1[:,1],wave1[:,2])
plt.plot(wave2[:,0],wave2[:,1],wave2[:,2])
ax.set_xlim([-5,5])
ax.set_ylim([-5,5])
ax.set_zlim([-5,5])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

rFP = array([30,0,0])
camDCM = identity(3)

wave1LOS =  rFP - wave1
wave1LOSHat = norm(wave1LOS)

wave2LOS =  rFP - wave2
wave2LOSHat = norm(wave2LOS)

# plt.figure()
# for i in range(0,len(wave1LOSHat)):
# 	plt.plot(wave1LOSHat[i,1]/wave1LOSHat[i,0],wave1LOSHat[i,2]/wave1LOSHat[i,0],
# 		'.',markersize=1,zorder=wave1LOSHat[i,0],color='blue')
# for i in range(0,len(wave1LOSHat)):
# 	plt.plot(wave2LOSHat[i,1]/wave2LOSHat[i,0],wave2LOSHat[i,2]/wave2LOSHat[i,0],
# 		'.',markersize=1,zorder=wave2LOSHat[i,0],color='green')
# plt.plot(wave2LOSHat[:,1]/wave2LOSHat[:,0],wave2LOSHat[:,2]/wave2LOSHat[:,0],
# 		'.',markersize=1,zorder=wave2LOSHat[:,0])
plt.xlim([-0.3,0.3])
plt.ylim([-0.3,0.3])


trace = go.Scatter3d(
    x=wave1[:,0], y=wave1[:,1], z=wave1[:,2],
    marker=dict(
        size=2,
        color='#DC143C',
        colorscale='Viridis',
    )
)
trace2 = go.Scatter3d(
    x=wave2[:,0], y=wave2[:,1], z=wave2[:,2],
    marker=dict(
        size=2,
        color='#32CD32',
        colorscale='Viridis',
    )
)
data = [trace,trace2]
layout=dict(title='Iris dataset',
	scene = dict(
    xaxis = dict(
        title='X AXIS',
        range = [-10,10]),
    yaxis = dict(
        title='Y AXIS',
        range = [-10,10]),
    zaxis = dict(
        title='Z AXIS',
        range = [-10,10]),)
	)
fig = dict(data=data,layout=layout)
offline.plot(fig, filename='pandas-brownian-motion-3d',  validate=False)
# plt.show()
pdb.set_trace()