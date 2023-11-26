# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:40:07 2022

@author: tanka
"""
total = 0


temp_data = [32.5, 31.2, 29.6, 30.7, 30.5, 31.2, 29.9]



for ix in range(len(temp_data)):
    print(f"Temperature of day {ix+1} is {temp_data[ix]} degC")
    total += temp_data[ix]
    
    
ave_temp = total / len(temp_data)
ave_temp = print(f"The average temperature for the week is {ave_temp:.2f} degC")