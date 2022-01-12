import math
import feuler

s = 0

for i in range(101):
    s+= i**2

p = (100*101)/2

print(p**2 - s)
