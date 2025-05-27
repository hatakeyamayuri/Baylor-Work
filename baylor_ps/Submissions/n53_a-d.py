#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:58:11 2023

@author: dittmann
"""

"""
This is a short program that finds Pythagorean Triples, which are sets of integers a, b, c
such that a^2 + b^2 = c^2, with c <= 100.

The output is lines where each line contains three integers, corresponding to a, b, and c.

The lines are not sorted intentionally.  They appear in order of increasing a.
"""

import math

counter = 0

smallest_b = 100
largest_b = 0

for a in range(1, 100):
    for b in range(a, 100):
        c = math.sqrt(a**2 + b**2)
        if int(c) == c and c <= 100:
            print(a, b, int(c))
            if b < smallest_b:
                smallest_b = b
            if b > largest_b:
                largest_b = b
            counter += 1

print("Smallest b value:", smallest_b)
print("Largest b value:", largest_b)

print("Line number:", counter)

"""
a) 52 lines. 
   First: 3, 4, 5. 
   Last: 65, 72, 97.

b) Smallest a: 3
   Largest a: 65

c) Smallest b: 4
   Largest b: 96

d) The program systematically checks through all unique, unordered combinations of a and b values to see if, when inputed into a^2 + b^2 = c^2, it will produce a c value that is an integer. The int(c) == c checks whether c is effectively an integer as int(c) will truncate c, cutting off all decimal digits and then comparing it to the original value before truncating to see if it changed. If true, c is effectively an integer and fufills a pythagorean triple.
"""