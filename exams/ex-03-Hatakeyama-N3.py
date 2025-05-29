#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl
import urllib.request #for fetching data
import sys

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data1a = urllib.request.urlopen("https://hep.baylor.edu/2360/data1a.txt", context=ctx)
data1b = urllib.request.urlopen("https://hep.baylor.edu/2360/data1b.txt", context=ctx)

Data1a = [] 
Data1b = []

#read first file and print contents
print("Data file:  data1a")
for line in data1a: 
    collision_str, detx_str, dety_str, energy_str = line.decode().split()
    collision = int(collision_str)
    detx = int(detx_str)
    dety = int(dety_str)
    energy = float(energy_str)
    Data1a.append((collision, detx, dety, energy))
    #print(f"{collision:10d}\t{detx:3d}\t{dety:3d}\t{energy:10.4f}")
    
			             
#read first file and print contents
print("Data file:  data1b")
for line in data1b: 
    collision_str, detx_str, dety_str, energy_str = line.decode().split()
    collision = int(collision_str)
    detx = int(detx_str)
    dety = int(dety_str)
    energy = float(energy_str)
    Data1b.append((collision, detx, dety, energy))
    #print(f"{collision:10d}\t{detx:3d}\t{dety:3d}\t{energy:10.4f}")

print(len(Data1a),len(Data1b))

Data1a_sorted = sorted(Data1a)
Data1b_sorted = sorted(Data1b)

#only altered below here.
energy_list = [] #list to hold energy difference

for i in range(len(Data1a_sorted)):
    #print(Data1a_sorted[i][0],Data1a_sorted[i][1],Data1a_sorted[i][2],Data1a_sorted[i][3])
    #print(Data1b_sorted[i][0],Data1b_sorted[i][1],Data1b_sorted[i][2],Data1b_sorted[i][3])

    #check if collsion number and coordinates match
    if (Data1a_sorted[i][0] == Data1b_sorted[i][0]) and (Data1a_sorted[i][1] == Data1b_sorted[i][1]) and (Data1a_sorted[i][2] == Data1b_sorted[i][2]): 
        energy_difference = Data1a_sorted[i][3] - Data1b_sorted[i][3] #calculates the difference in energy
        energy_list.append(energy_difference) 

         #prints the collsion number and coordinates (from Data1a_sorted since its the same as Data1b_sorted) and their respective energy difference
        print(Data1a_sorted[i][0], Data1a_sorted[i][1], Data1a_sorted[i][2], energy_list[i])