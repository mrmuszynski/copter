#! /usr/bin/env python3

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy import cos, sin, deg2rad, array,vstack,empty,pi, sqrt
from numpy import identity
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
import pdb



X = empty((0,3),float)
for i in range(0,180):
	phi = deg2rad(i)
	theta = deg2rad(20*i)
	x = array([
		cos(theta),
	    sin(theta),
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