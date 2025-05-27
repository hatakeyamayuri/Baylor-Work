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

def pytriples(max_c):
    counter = 0
    count_c = 0

    for a in range(1, max_c):
        amax = max_c/(math.sqrt(2))
        if a >= amax:
            break
        for b in range(a, max_c):
            if a != b:
                c = math.sqrt(a**2 + b**2)
                count_c += 1
                if int(c) == c and c <= max_c:
                    for i in range(2, max_c):
                        #print(i, a%i, b%i, int(c%i))
                        if ((a%i) == (b%i) == int(c%i)) and ((a%i) == 0):
                            #print("here", a, b)
                            break
                        elif i == max_c-1:
                            print(a, b, int(c))
                            counter += 1

    print("Line number:", counter)
    print("Times c ran:", count_c)

pytriples(100)