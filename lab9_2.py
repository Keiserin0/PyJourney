# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:53:07 2022

@author: tanka
"""

day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
temp_data = []


for ix in range(len(day)):
    temp_data.append(float(input(f"Please enter the temperature for {day[ix]}: ")))
    
for i, data in enumerate(zip(day, temp_data)):
    print(f"Temperature on {day[i]} is {temp_data[i]} degC")
    