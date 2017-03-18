# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:50:25 2017

@author: Dominik
"""


import plotly.plotly as py
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        size=[40, 60, 80, 100],
    )
)

data = [trace0]
py.plot(data, filename='bubblechartsize')