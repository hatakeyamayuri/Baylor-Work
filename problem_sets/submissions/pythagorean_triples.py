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

'''
Orders the output from smallest largest c value
Decreses number of times explicit c calulation done through even-odd properties
'''

import math

counter = 0
count_c = 0

for c in range(1, 101): #loops through potential c values
    for a in range(1, 100):

        #if c is even, both a&b must be even or odd. 
        #if c is odd, a & b be have different even-odd classifications. 
        if c % 2 == 0:
            start_b = a+2 # if even, the starting b value is the same even-odd classification as the a value 
        else:
            start_b = a+1 # if odd, the starting b value is a different even-odd classification as the a value 
        for b in range(start_b, 100, 2): #b is looped for every other value so the starting b value's even-odd classification is kept for all consecutive b values
            count_c += 1
            if math.sqrt(a**2 + b**2) == c: #compares the calculated c value to the integer c value
                print(a, b, int(c))
                counter += 1

print("Line number:", counter)
print("Times c ran:", count_c)