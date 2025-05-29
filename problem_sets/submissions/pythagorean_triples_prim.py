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
    '''
    Finds primitive pythagorean triples
    Decreses number of times explicit c calulation done
    '''

    counter = 0
    count_c = 0

    for a in range(1, max_c):

        #sets a limit on the number of a values to test.
        amax = max_c/(math.sqrt(2))  #calculation for max a value
        if a >= amax:#if a is greater than the limit, breaks loop as all triples have been found
            break

        for b in range(a+1, max_c): #loops hrough all b values where it is a<b<max_c so no duplicates and a!=b (as no c values will be integers from that ratio)
            c = math.sqrt(a**2 + b**2)  #calculates c value using a & b 
            count_c += 1
            if int(c) == c and c <= max_c: #checks if a, b, c is pythagorean triple within max c constraint
                for i in range(2, c): #loops through to 2 and c (largest of a, b, c). i acts as divisor
                    #print(i, a%i, b%i, int(c%i))
                    if ((a%i) == (b%i) == int(c%i) == 0): #checks if a, b, c are ever divisible by the same divisor
                        #print("here", a, b)
                        break #if yes, not a primitive pythagorean triple
                    if i == max_c-1: #checks if i is in its last iteration, meaning it is primitive pythagorean triple
                        print(a, b, int(c)) 
                        counter += 1

    print("Line number:", counter)
    print("Times c ran:", count_c)

pytriples(100)