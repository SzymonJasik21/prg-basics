###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
# d = 3.57 × √h
#d is the distance to the horizon in kilometers
#h is the height of the observer in meters
#Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:

#You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
#You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

import math 
h=20
total = 8000000000
north = 7200000000
south = ...
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
d=3.57*math.sqrt(h)

