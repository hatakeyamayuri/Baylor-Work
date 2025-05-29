#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
altered to reject roman numerals if values meant for 'subtraction' are not a valid
(specfically: if the values are not in a 1:5 ratio (as opposed to 1:10))
'''

import sys

#given dictionary of individual roman number values
roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000
                  }

int_value = 0

user_input = input("Enter Roman Number: ").upper()

#print("len(user_input): ",len(user_input))

for i in range(len(user_input)):
    print(user_input[i])
    if user_input[i] in roman_numerals:
        #print("i,int_value: ",i,int_value)

        #checks if the next value in the sequence of the numerals (if there is one) is less than the current numeral
        if i + 1 < len(user_input) and \
                roman_numerals[user_input[i]] < roman_numerals[user_input[i + 1]]:
            
            #only part altered. calculates and checks whether the subtractive values are in a 1:5 ratio
            temp_calc = roman_numerals[user_input[i + 1]] / roman_numerals[user_input[i]]
            if temp_calc == 5:
                # subtraction
                int_value -= roman_numerals[user_input[i]]
            else:
                print("Invalid input.")
                sys.exit()
        else:
            # addition
            int_value += roman_numerals[user_input[i]]
        print(int_value) #prints current accumulated value of the numeral
    else:
        print("Invalid input.")
        sys.exit()

print("The integer value is: ", int_value)
