sq = 2
t = 1
i = 3

while sq < 1001:
    t+=i
    t+=i+sq
    t+=i+(2*sq)
    t+=i+(3*sq)
    i = i+(3*sq) + sq + 2
    sq+=2

print(t)


