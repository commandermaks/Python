""" 
Program : sphere.py
Author : MD MAKSUDUR RAHMAN
Date : 27/03/2026
The purpose of this program is to calculate and display the surface area and volume of a sphere given its radius   .
"""
# Import math module at he start of the program to use math.pi
import math  

# Input the radius of the sphere ( a floating point number)
radius = float(input("Enter the radius of the sphere: "))

# Calculations for diameter, circumference, surface area and volume of the sphere 
diameter = 2 * radius
circumference = diameter * math.pi
surface_area = 4 * math.pi * radius * radius
volume = (4/3) * math.pi * radius * radius * radius

# Output
print("Diameter:", diameter)
print("Circumference:", circumference)
print("Surface Area:", surface_area)
print("Volume:", volume)