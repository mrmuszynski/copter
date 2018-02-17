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


X = empty((0,3),float)
for i in range(0,180):
	phi = deg2rad(i)
	theta = deg2rad(20*i)
	x = array([
		sin(phi)*cos(theta),
	    sin(phi)*sin(theta),
	    cos(phi) - 2
	    ])
	X = vstack([X,x])


for i in range(0,180):
	phi = deg2rad(i)
	theta = deg2rad(20*i)
	x = array([
		sin(phi)*cos(theta),
	    sin(phi)*sin(theta),
	    phi
	    ])
	X = vstack([X,x])

# pdb.set_trace()



trace = go.Scatter3d(
    x=X[:,0], y=X[:,1], z=X[:,2],
    marker=dict(
        size=2,
        color='#DC143C',
        colorscale='Viridis',
    )
)
# trace2 = go.Scatter3d(
#     x=wave2[:,0], y=wave2[:,1], z=wave2[:,2],
#     marker=dict(
#         size=2,
#         color='#32CD32',
#         colorscale='Viridis',
#     )
# )
# data = [trace,trace2]
data = [trace]
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
# plt.show()
pdb.set_trace()