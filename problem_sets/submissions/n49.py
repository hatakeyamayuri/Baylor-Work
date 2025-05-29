#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 08:10:46 2022

@author: dittmann
"""

'''
creates 6 different colored spirals

'''
import math
import matplotlib.pyplot as plt

#list of colors for different curves
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

base_scale = 0.01
base_b = -0.04
base_start = 250
base_end = 1500

#loops through once for each spiral
for i in range(len(colors)): 
    #within loop so it resets and doesn't carry on previous spiral's points
    x_values = []
    y_values = []

    #alters the earlier defined base values (at varying rates) according to which spiral it is creating to create unique spirals
    scale = (.01 * i) + base_scale
    b = -(.01 * i) + base_b
    start = (50 * i) + base_start
    end = -(100 * i) + base_end

    #given portion. complies the points into lists to create the spirals
    for n in range(start, end + 1):
        t = scale*n
        x = math.exp(b*t) * math.cos(t)
        y = -math.exp(b*t) * math.sin(t)
        x_values.append(x)
        y_values.append(y)

    label = f"Spiral {i+1}" #creates the string for label 
    plt.scatter(x_values, y_values, color=colors[i], label=label) #plots the points with color pulled from earlier 'colors' list

plt.legend() #turns the assigned labels into a color legend
plt.show()