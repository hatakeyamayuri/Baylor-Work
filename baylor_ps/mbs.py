#!/usr/bin/env python3
# -*- coding: utf-8 -*-
  
# Import necessary libraries
from PIL import Image
from numpy import array
import colorsys
  
# setting the width of the output image as 1024
WIDTH = 1024
XSIZE = WIDTH
YSIZE = WIDTH/2
scl = .000005
xoff = -0.3486263378412691
yoff = -0.6065394023439323
  
# a function to return a tuple of colors
# as integer value of rgb
def rgb_conv(i):
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5))
    return tuple(color.astype(int))
  
def mf(x, y):
    c0 = complex(x, y)
    c = 0
    for i in range(1, 400):
        if abs(c) > 2:
            return rgb_conv(i)
        c = c * c + c0
    return (0, 0, 0)
  
# creating the new image in RGB mode
img = Image.new('RGB', (WIDTH, int(WIDTH / 2)))
pixels = img.load()
  
for x in range(img.size[0]):
  
    # displaying the progress as percentage
    print("%.2f %%" % (x / WIDTH * 100.0)) 
    for y in range(img.size[1]):
        pixels[x, y] = mf( scl*(x-XSIZE/2)/XSIZE + xoff,
                           scl*(y-YSIZE/2)/YSIZE/2 + yoff)
  
img.show()
img.save("ps-05.png")