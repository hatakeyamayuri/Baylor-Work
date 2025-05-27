#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

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

print("len(user_input): ",len(user_input))

for i in range(len(user_input)):
    print(user_input[i])
    if user_input[i] in roman_numerals:
        print("i,int_value: ",i,int_value)
        if i + 1 < len(user_input) and \
                roman_numerals[user_input[i]] < roman_numerals[user_input[i + 1]]:
            temp_calc = roman_numerals[user_input[i + 1]] % roman_numerals[user_input[i]]
            if temp_calc == 2 or temp_calc == 5:
                # subtraction
                int_value -= roman_numerals[user_input[i]]
            else:
                print("Invalid input.")
                sys.exit()
        else:
            # addition
            int_value += roman_numerals[user_input[i]]
        print(int_value)
    else:
        print("Invalid input.")
        sys.exit()

print("The integer value is: ", int_value)
