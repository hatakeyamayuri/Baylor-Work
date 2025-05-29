#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

'''
Lists Switzerland cities in order of how far they are from Bern
'''

# Python dictionary of Swiss cities and towns (latitude and longitude)
swiss_cities = {
    "Lugano":     (46.00108, 8.96199),
    "Winterthur": (47.49874, 8.72555),
    "Geneva":     (46.20506, 6.14475),
    "Zug":        (47.16172, 8.51944),
    "Basel":      (47.55911, 7.58685),
    "Lausanne":   (46.52012, 6.63069),
    "Interlaken": (46.68610, 7.86370),
    "Luzern":     (47.04955, 8.30797),
    "Montreux":   (46.43071, 6.91182),
    "St. Gallen": (47.42378, 9.37435),
    "Sion":       (46.23333, 7.36033),
    "Davos":      (46.80272, 9.83597),
    "Thun":       (46.75806, 7.62819),
    "Zermatt":    (46.02125, 7.74973),
    "Spiez":      (46.68868, 7.67907),
    "Bern":       (46.94871, 7.44986),
    }

base_lat, base_long = swiss_cities["Bern"] #the lat & long of Bern
distance_list = [] #to hold the distances of the cities to Bern
city_distances = {} #to hold which city corresponds to what distance from Bern

for city in swiss_cities:
    lat, long = swiss_cities[city] #finds the lat and long of each city to be tested
    distance = math.sqrt((lat - base_lat)**2 + (long - base_long)**2) #calculates the distance of the city to Bern
    distance_list.append(distance) #puts that distance in list
    city_distances[distance] = city #saves the distance in relation to which city

distance_list.sort() #sorts the distances from smallest (closest) to largest (farthest)

for distance in distance_list: #going from closest to farthest city
    city = city_distances[distance] #finds which city the distance corresponds to

    #printing info
    lat, long = swiss_cities[city]
    print(f"{city} is located at {lat}° latitude and {long}° longitude.")