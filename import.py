# Three types of import a module
# Generic import
# Function import
# Universal import

# import random  # Generic import example
#
# print(random.randint(1,10))  # both arguments are inclusive
#
from random import randint  # Function import example
# print(randint(13,20))
#
# from random import *  # Universal import example
# print(randint(30,43))
#
# print(random()) # return a float value ->greater than 0 and less than 1

#Calculate Miles per Gallon
# formula MPG=miles driven/gallons used.
number_of_gallon_per_gas=randint(10,25)
miles=randint(200,400)
print(number_of_gallon_per_gas,miles)
print(miles//number_of_gallon_per_gas)
