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

for c in range(1, 101):
    for a in range(1, 100):
        for b in range(a, 100):
            if math.sqrt(a**2 + b**2) == c:
                print(a, b, int(c))
                counter += 1

print("Line number:", counter)