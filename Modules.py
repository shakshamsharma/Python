#Built-in Modules
"""
import math
print(math.sqrt(5))
"""

#Pick random number
"""
import random
print(random.randint(1,10))
"""

#import current date and time 
"""
import datetime
print(datetime.datetime.now())
"""

#Import Specific Functions
"""
from math import sqrt
print(sqrt(25))
"""

#Import Multiple Functions
"""
from math import sqrt, factorial
print(sqrt(25))
print(factorial(5))
"""

#Aliases
#Sometimes module names are long.
"""
import datetime as dt
print(dt.datetime.now())
"""

#Another Example
"""
import math as m
print(m.sqrt(25))
"""

#Import Everything
"""
from math import *
print(sqrt(25))
print(factorial(5))
"""

#Practice - 1
"""
import math
print(math.sqrt(5))
print(math.factorial(5))

from random import randint
print(randint(1,100))

import datetime 
print(datetime.datetime.now())

import math as m
print(m.sqrt(25))
"""
"""
import calculator
print(calculator.add(10,30))
"""