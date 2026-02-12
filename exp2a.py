
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 10:30:34 2026

@author: Agce
"""


year = int(input("Enter year."))
if (year % 400 == 0) or (year % 4 == 0 and year % 100!= 0):
       print("lEAP yEAR")
else:    
       print("Not a Leap Year")
  
            
  