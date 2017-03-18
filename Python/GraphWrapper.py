# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 18:50:25 2017

@author: Dominik
"""

import plotly.plotly as py
import plotly.graph_objs as go

'''
plotly.tools.set_credentials_file(username='dkoscica', api_key='GBBHXNPiEhUfCuk542CW')

labels =  ['Pero Drone', 'Okrutna budilica', 'NikolaM #losekeys', 'Emanuel Borić', 'Dolores Skugor', 
'#Fit_at_Work', 'VirtualKeyboard', 'NanotechServices', 'Coffeex', 'Coffeex', 'Univ. Prevoditelj']
values = [11, 9, 6, 5, 5,4, 4, 4, 3, 2]

fig = {
    'data': [{'labels': labels,
              'values': values,
              'type': 'pie'}],
    'layout': {'title': 'Top 10 followera koji su koristili #Stick2Me tag'}
     }

py.iplot(fig)
'''

import plotly.plotly as py
import plotly.graph_objs as go



data = [go.Bar(
            x=['giraffes', 'orangutans', 'monkeys'],
            y=[20, 14, 23]
    )]

py.iplot(data, filename='basic-bar')