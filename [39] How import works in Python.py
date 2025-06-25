# Importing in python is the process of loading code from a Python Module into the current script.

# math
import math
result = math.sqrt(9)
print(result)

# from keyword
from math import sqrt
result = sqrt(9)
print(result)

from math import sqrt,pi
result = sqrt(9)
print(result)
print(pi)

from math import sqrt,pi
result = sqrt(9) * pi
print(result)

#importing everything
from math import *
result = sqrt(9)
print(result)
print(pi)

# as keyword
import math as m
result = m.sqrt(9)
print(result)
print(pi)

from math import pi,sqrt as s
result = s(9) *pi
print(result) # here pi is automatically imported

# The dir function
import math
print(dir(math)) # dir function means ex. represents all the math functions

import math
print(dir(math))
print(math.nan , type(math.nan))
