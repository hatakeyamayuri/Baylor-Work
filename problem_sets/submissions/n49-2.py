#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 08:10:46 2022

@author: dittmann
"""

'''
creates 6 different colored spirals
dictionary-using version
'''

import math
import matplotlib.pyplot as plt

#dictionary of parameters. each index for each spiral
parameters = {
    "scale" : (0.01, 0.025, 0.035, 0.04, 0.06, .07),
    "b" : (-0.05, -0.03, -0.04, -0.08, -0.06, -0.02),
    "start" : (100, 250, 300, 150, 600, 800),
    "end" : (1200, 1300, 1100, 1750, 1800, 900),
    "color" : ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
}

#loops through once for each spiral
for i in range(len(parameters["color"])): 
    #within loop so it resets and doesn't carry on previous spiral's points
    x_values = []
    y_values = []

    #given portion. complies the points into lists to create the spirals
    for n in range(parameters["start"][i], parameters["end"][i] + 1):
        t = parameters["scale"][i]*n
        x = math.exp(parameters["b"][i]*t) * math.cos(t)
        y = -math.exp(parameters["b"][i]*t) * math.sin(t)
        x_values.append(x)
        y_values.append(y)

    label = f"Spiral {i+1}" #creates the string for label 
    plt.scatter(x_values, y_values, color=parameters["color"][i], label=label) #plots the points with color pulled from earlier 'colors' list

plt.legend() #turns the assigned labels into a color legend
plt.show()