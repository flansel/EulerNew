import math

rn = [1,5,10,50,100,500,1000]

#DCXCII

def val(s):
    s =s.replace("\n", "")
    s =s.replace("I","0")
    s =s.replace("V","1")
    s =s.replace("X","2")
    s =s.replace("L","3")
    s =s.replace("C","4")
    s =s.replace("D","5")
    s =s.replace("M","6")

    tval = 0
    
    for i in range(0,len(s)-1):
        if rn[int(s[i+1])] > rn[int(s[i])]:
            tval -= rn[int(s[i])]
        else:
            tval += rn[int(s[i])]
    tval += rn[int(s[len(s)-1])]
    return tval

def cvt(v):
    r = ""
    vs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    vsl = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    while v > 0:
        for i,x in enumerate(vs):
            if v >= x:
                v -= x
                r += vsl[i]
                break
    return r

f = open("roman.txt", "r")
ans = 0

for line in f.readlines():
    x = val(line)
    line = line.replace("\n", "")
    ns = cvt(x)
    ans += (len(line) - len(ns))
    print(line.replace("\n", ""), ns, x)
print(ans)
