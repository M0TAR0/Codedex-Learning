# Program to practice importing modules
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets) #Select Random planet from planets list
is_a_planet = True

#Calculate radius of the planet
if random_planet == "Mercury":
    r = 2440
elif random_planet == "Venus":
    r = 6052
elif random_planet == "Earth":
    r = 6371
elif random_planet == "Mars":
    r = 3390
elif random_planet == "Saturn":
    r = 58232
else: 
    print("Oops! An error ocurred")
    is_a_planet = False

if is_a_planet:
    radius = 4 * pi * pow(r, 2)
    print("Your planet \"" + random_planet + "\" has an area of:", round(radius), "m2")
