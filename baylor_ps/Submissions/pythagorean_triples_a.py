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
                    print(a, b, int(c))
                    counter += 1
    print("Line number:", counter)
    print("Times c ran:", count_c)

pytriples(10000)

"""
a) 52 lines. 
   First: 3, 4, 5. 
   Last: 65, 72, 97.

b) Smallest a: 3
   Largest a: 65

c) Smallest b: 4
   Largest b: 96

d) The program systematically checks through all unique(even when unordered) combinations of a and b values to see if, when inputed into a^2 + b^2 = c^2, it will produce a c value that is an integer. The int(c) == c checks whether c is effectively an integer as int(c) will truncate c, cutting off all decimal digits and then comparing it to the original value before truncating to see if it changed. If true, c is effectively an integer and fufills a pythagorean triple.

f) The line "c = math.sqrt(a**2 + b**2)" ran 4950 times.

g) After improvments, the line "c = math.sqrt(a**2 + b**2)" ran 4445 times.

h) 12471 triples. 
   45699873 times.
   13 seconds.
"""