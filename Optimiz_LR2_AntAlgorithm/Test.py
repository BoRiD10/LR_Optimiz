import numpy as np
import random
import time
import plotly
import plotly.graph_objs as go
import pylab
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.arange (0, 10, 0.5)
y = np.arange (0, 10, 0.5)
z = np.arange (5, 10, 0.5)

fig1 = go.Scatter3d(x=x,
                    y=y,
                    z=z,
                    marker=dict(opacity=0.9,
                                reversescale=True,
                                colorscale='Blues',
                                size=5),
                    line=dict (width=0.02),
                    mode='markers')

#Make Plot.ly Layout
mylayout = go.Layout(scene=dict(xaxis=dict( title="curb-weight"),
                                yaxis=dict( title="horsepower"),
                                zaxis=dict(title="price")),)

#Plot and save html
plotly.offline.plot({"data": [fig1],
                     "layout": mylayout},
                     auto_open=True,
                     filename=("3DPlot.html"))
