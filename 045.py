import math

fnd = 0
i = 1
tn = 1

while fnd < 3:
    pent = (1 + math.sqrt(1+(24*i)))/6
    hexa = (1 + math.sqrt(1+(8*i)))/4
    if pent == int(pent) and hexa == int(hexa):
        print(i, tn)
        fnd += 1
    tn += 1
    i = (tn*(tn+1))/2
"""
    if hexa == int(hexa):
        print("hex: ", i)
    if pent == int(pent):
        print("pent: ", i)
"""
