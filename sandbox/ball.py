#! /usr/bin/env python3
###############################################################################
#
#	Title   : main.py
#	Author  : Matt Muszynski
#	Date    : 01/30/18
#	Synopsis: Sandbox script for copter
#
###############################################################################

import sys
sys.path.insert(0, '../util')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy.linalg import norm
import pdb
from numpy import array, sin, cos, vstack, empty, pi, arcsin, arccos, zeros
from numpy import rad2deg, deg2rad, ceil, cross, linspace, hstack, ones
from numpy import sqrt
from util import r3
from numpy.linalg import norm
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
import pdb


theta = linspace(0,2*pi)
plt.plot(cos(theta),sin(theta))
plt.axis('equal')
plt.plot(0.5*ones(len(theta)),linspace(-1,1),color='orange')
plt.plot(-0.5*ones(len(theta)),linspace(-1,1),color='orange')
plt.plot(linspace(-1,1),-0.86474*ones(len(theta)),color='orange')
plt.plot(linspace(-1,1),0.86474*ones(len(theta)),color='orange')


X = []
Y = []
Z = []
plt.figure()
theta = linspace(-pi/2,pi/2)
X = hstack([X,zeros(len(theta))])
Y = hstack([Y,0.4+0.6*cos(theta)])
Z = hstack([Z,0.84*sin(theta)])
theta = linspace(pi/2,pi)
X = hstack([X,zeros(len(theta))])
Y = hstack([Y,0.4+0.2*cos(theta)])
Z = hstack([Z,0.09 + 0.75*sin(theta)])
theta = linspace(pi,3*pi/2)

X = hstack([X,-0.2-0.2*cos(theta)])
Y = hstack([Y,0.2+zeros(len(theta))])
Z = hstack([Z,0.09+0.75*sin(theta)])

alpha = 36+72

stack = vstack([X,Y,-Z])
rotStack = r3(deg2rad(alpha)).dot(stack)

theta = linspace(-5*pi/4,3*pi/4+2*pi+deg2rad(alpha),100)
Xspiral = sqrt(0.08)*cos(theta)
Yspiral = sqrt(0.08)*sin(theta)
Zspiral = -0.66+0.01*linspace(0,66*2,100)

X = hstack([X,Xspiral])
Y = hstack([Y,Yspiral])
Z = hstack([Z,Zspiral])

spiralStack = vstack([Xspiral,Yspiral,Zspiral])
rotSpiralStack = r3(deg2rad(alpha)).dot(spiralStack)

X = hstack([X,rotStack[0]])
Y = hstack([Y,rotStack[1]])
Z = hstack([Z,rotStack[2]])

theta = linspace(-5*pi/4,3*pi/4+2*pi+deg2rad(alpha),100)
X = hstack([X,sqrt(0.08)*cos(theta)])
Y = hstack([Y,sqrt(0.08)*sin(theta)])
Z = hstack([Z,-0.66+0.01*linspace(0,66*2,100)])

X = hstack([X,rotSpiralStack[0]])
Y = hstack([Y,rotSpiralStack[1]])
Z = hstack([Z,rotSpiralStack[2]])

stack1 = vstack([X,Y,Z])
rotStack1 = r3(deg2rad(2*alpha)).dot(stack1)
stack2 = vstack([X,Y,Z])
rotStack2 = r3(deg2rad(4*alpha)).dot(stack2)
stack3 = vstack([X,Y,Z])
rotStack3 = r3(deg2rad(6*alpha)).dot(stack3)
stack4 = vstack([X,Y,Z])
rotStack4 = r3(deg2rad(8*alpha)).dot(stack4)

X = hstack([X,rotStack1[0]])
Y = hstack([Y,rotStack1[1]])
Z = hstack([Z,rotStack1[2]])

X = hstack([X,rotStack2[0]])
Y = hstack([Y,rotStack2[1]])
Z = hstack([Z,rotStack2[2]])

X = hstack([X,rotStack3[0]])
Y = hstack([Y,rotStack3[1]])
Z = hstack([Z,rotStack3[2]])

X = hstack([X,rotStack4[0]])
Y = hstack([Y,rotStack4[1]])
Z = hstack([Z,rotStack4[2]])



plt.axis('equal')


X0 = vstack([X,Y,Z]).T
# X1 = (r3(deg2rad(360/5)).dot(X0.T)).T
# X2 = (r3(deg2rad(360/5)).dot(X1.T)).T
# X3 = (r3(deg2rad(360/5)).dot(X2.T)).T
# X4 = (r3(deg2rad(360/5)).dot(X3.T)).T
# X5 = vstack([Z,-X,-Y]).T
# X6 = (r3(deg2rad(360/5)).dot(X5.T)).T
# X7 = (r3(deg2rad(360/5)).dot(X6.T)).T
# X8 = (r3(deg2rad(360/5)).dot(X7.T)).T
# X9 = (r3(deg2rad(360/5)).dot(X8.T)).T

# X = vstack([X0,X1,X2,X3,X4,X5,X6,X7,X8,X9])
trace0 = go.Scatter3d(
    x=X0[:,0], y=X0[:,1], z=X0[:,2],
    marker=dict(
        size=2,
        color='#DC143C',
        colorscale='Viridis',
    )
)
# trace1 = go.Scatter3d(
#     x=X1[:,0], y=X1[:,1], z=X1[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace2 = go.Scatter3d(
#     x=X2[:,0], y=X2[:,1], z=X2[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace3 = go.Scatter3d(
#     x=X3[:,0], y=X3[:,1], z=X3[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace4 = go.Scatter3d(
#     x=X4[:,0], y=X4[:,1], z=X4[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace5 = go.Scatter3d(
#     x=X5[:,0], y=X5[:,1], z=X5[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace6 = go.Scatter3d(
#     x=X6[:,0], y=X6[:,1], z=X6[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace7 = go.Scatter3d(
#     x=X7[:,0], y=X7[:,1], z=X7[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace8 = go.Scatter3d(
#     x=X8[:,0], y=X8[:,1], z=X8[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )
# trace9 = go.Scatter3d(
#     x=X9[:,0], y=X9[:,1], z=X9[:,2],
#     marker=dict(
#         size=2,
#         color='#DC143C',
#         colorscale='Viridis',
#     )
# )


data = [
	trace0,
	# trace1,
	# trace2,
	# trace3,
	# trace4,
	# trace5,
	# trace6,
	# trace7,
	# trace8,
	# trace9
	]
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
        range = [-10,10]),
    aspectmode = 'cube'),

	)
fig = dict(data=data,layout=layout)
offline.plot(fig, filename='pandas-brownian-motion-3d',  validate=False)



pdb.set_trace()