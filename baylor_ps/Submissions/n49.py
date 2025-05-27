#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: all of us
"""

import math
import matplotlib.pyplot as plt

colors = ['black', 'blue', 'purple', 'orange', 'green', 'red']

params = [
    (0.006, -0.01, 250, 1000),
    (0.01, -0.02, 500, 800),
    (0.015, -0.04, 300, 600),
    (0.008, -0.08, 180, 700),
    (0.012, -0.1, 200, 500),
    (0.01, -0.06, 250, 1500)
    ]


"""
scale = 0.5
b = -0.04
start = 250
end = 200
"""

for i, (scale, b, start, end) in enumerate(params):
    
    print(scale, b, start, end)
    name="aaa"
    
    #==== chunck you want to repeat
    x_values = []
    y_values = []

    for n in range(start, end + 1):
        t = scale*n
        x = math.exp(b*t) * math.cos(t)
        y = -math.exp(b*t) * math.sin(t)
        x_values.append(x)
        y_values.append(y)
        
    plt.scatter(x_values, y_values, label=f'Spiral {i+1}', color=colors[i])

#=====

plt.title("Spirals")
plt.legend()
plt.show()