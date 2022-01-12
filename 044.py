import math

p = [(n * (3*n -1))/2 for n in range(1,10000)]

for x in p:
    for y in p:
        s = x-y
        a = x+y
        if s <= 0:
            break
        s = (1+math.sqrt(1+(24*s)))/6

        if s == int(s):
            a = (1+math.sqrt(1+(24*a)))/6
            
            if a == int(a):
                print(x,y,x+y,x-y)

