#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

roman_numerals = {"I" : 1,
                  "V" : 5,
                  "X" : 10,
                  "L" : 50,
                  "C" : 100,
                  "D" : 500,
                  "M" : 1000,
                  "_" : "*1000"
                  }

int_value = 0
value_list = []

raw_user_input = input("Enter Roman Number: ").upper()
user_input = list(raw_user_input)
underscore = raw_user_input.count("_")

print("len(user_input): ",len(raw_user_input))

for i in range(len(user_input)-underscore):
    if user_input[i] in roman_numerals:
        print(i, user_input[i])
        if i < len(user_input) and user_input[i] == "_":
            value_list.append(roman_numerals[user_input[i+1]] * 1000)
            user_input.pop(i+1)
        else:
            value_list.append(roman_numerals[user_input[i]])
    else:
        print("Invalid input.")
        sys.exit()

print(value_list)

for i in range(len(value_list)):
    print("i,int_value: ", i, int_value)
    if (i + 1) < len(user_input):
        temp_calc = value_list[i + 1] % value_list[i]
        if value_list[i] < value_list[i+1] and (temp_calc == 2 or temp_calc == 5):
                # subtraction
                int_value -= value_list[i]
        else:
            print("Invalid input.")
            sys.exit()
    else:
        # addition
        int_value += value_list[i]
    print(int_value)

print("The integer value is: ", int_value)