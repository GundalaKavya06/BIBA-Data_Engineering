from math import *
print(sqrt(16)) #4.0
print(factorial(6)) #720


#provides directories list
import sys
print(sys.path)

#renaming module name
import math as mt
print(mt.sqrt(16))
print(mt.factorial(6))


import math
print(math.sqrt(25)) 
# using pi function contained in math module
print(math.pi) 
# 2 radians = 114.59 degrees
print(math.degrees(2))  
# 60 degrees = 1.04 radians
print(math.radians(60))  
# Sine of 2 radians
print(math.sin(2))  
# Cosine of 0.5 radians
print(math.cos(0.5))  
# Tangent of 0.23 radians
print(math.tan(0.23)) 
# 1 * 2 * 3 * 4 = 24
print(math.factorial(4))  



# importing built in module random
import random
# printing random integer between 0 and 5
print(random.randint(0, 5))  
# print random floating point number between 0 and 1
print(random.random())  
# random number between 0 and 100
print(random.random() * 100)  
List = [1, 4, True, 800, "python", 27, "hello"]
# using choice function in random module for choosing 
# a random element from a set such as a list
print(random.choice(List)) 




from datetime import date
import time
# Returns the number of seconds since the
# Unix Epoch, January 1st 1970
print(time.time())   #1702900562.4174562
# Converts a number of seconds to a date object
print(date.fromtimestamp(95455423))   #1973-01-10
