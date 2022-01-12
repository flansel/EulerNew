sy = 1900
ey = 2001
sc = 0
ms = [31,28,31,30,31,30,31,31,30,31,30,31]
sd = 1
mt = 0
dom = 1

for year in range(sy,ey):
    if year % 400 == 0 or (year%4 == 0 and year%100 != 0):
        ms[1] = 29
        days = 366
    else:
        ms[1] = 28
        days = 365
    
    for i in range(days):
        print(dom,mt+1,year)
        if sd == 0 and year > 1900 and dom == 1:
            sc += 1
        sd += 1
        sd %= 7
        if dom == ms[mt]:
            mt += 1
            dom = 0
        dom +=1
    mt = 0
    dom = 1

print(sc)
