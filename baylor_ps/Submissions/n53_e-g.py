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
    for a in range(3, 66):
        for b in range(a, 97):
            if a != b:
                c = math.sqrt(a**2 + b**2)
                count_c += 1
                if int(c) == c and c <= max_c:
                    print(a, b, int(c))
                    counter += 1
    print("Line number:", counter)
    print("Times c ran:", count_c)

pytriples(100)

"""
f) The line "c = math.sqrt(a**2 + b**2)" ran 4950 times.

g) After improvments, the line "c = math.sqrt(a**2 + b**2)" ran 4095 times.
"""