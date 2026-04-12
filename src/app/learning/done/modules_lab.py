import math
from platform import system
import random as rd


x = 2
y = 10
c = math.pow(x, y)
print(c)

current_os = system()
print(current_os)

knowleges = ['Study', 'Coding', 'Health']
print(rd.choice(knowleges))
