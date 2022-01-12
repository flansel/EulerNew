import math
f = open("base_exp.txt", "r")

m = 0
mi = 0

for i in range(1000):
    s = f.readline().split(",")
    s[0] = int(s[0])
    s[1] = int(s[1])
    x = s[1] * math.log(s[0])
    print(s, x)
    if x > m:
        m = x
        mi = i+1
print(m,mi)
