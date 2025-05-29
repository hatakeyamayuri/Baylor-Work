#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
altered from n50.py to accept roman numerals to 3,999,999 with input using underscores ('_')
'''

import sys

roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000,
                  "_" : "*1000" #added _ as key so it wouldn't register as a invalid character
                  }

int_value = 0
value_list = []

raw_user_input = input("Enter Roman Number: ").upper()
user_input = list(raw_user_input) #converts the string the user sends to a list of each character individually
underscore = raw_user_input.count("_")

#print("len(user_input): ",len(raw_user_input))

#puts all numeral values into a list with their arabic values. (calculates for the underscore)
for i in range(len(user_input)-underscore): #loops for every non-underscore chracter
    if user_input[i] in roman_numerals: #checking if character is valid
        #print(i, user_input[i])
        if i < len(user_input) and user_input[i] == "_": #checks if the character is an underscore in a valid position
            value_list.append(roman_numerals[user_input[i+1]] * 1000) #appends the next character's value * 1000 to the list of arabic values
            user_input.pop(i+1) #deletes the next character so it wont' be reused individually
        else:
            value_list.append(roman_numerals[user_input[i]]) #if not an underscore, simply added to value_list
    else:
        print("Invalid input.")
        sys.exit()

print(value_list)

#finds final arabic value through + and - of consecutive values
for i in range(len(value_list)):
    #print("i,int_value: ", i, int_value)
    if int_value < 4000000000: #checks if value is under threshold
        if (i + 1) < len(user_input): #checks that i is not the last value 

            #same as n50.py in checking if the subtracting values are at 1:5 ratio.
            temp_calc = value_list[i + 1] / value_list[i]
            if value_list[i] < value_list[i+1] and temp_calc == 5:
                    # subtraction
                    int_value -= value_list[i]
            else:
                print("Invalid input.")
                sys.exit()
        else:
            # addition
            int_value += value_list[i]
    else:
                print("Invalid input.")
                sys.exit()
    print(int_value) #shows current, running total

print("The integer value is: ", int_value)