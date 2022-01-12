import math
cf = [2,1,2]

tr = 4
while len(cf) < 101:
    x = [1,1,tr]
    cf += x
    tr += 2

#print(cf)

i = 99
den = cf[i]
num = 1
ans = 0 

while i > 1:
    num += cf[i-1]*den
    tmp = den
    den = num
    num = tmp
    #print(num,den,num/den)
    i -= 1
num += 2*den

print(num/den)

for c in str(num):
    ans += int(c)
print(ans)
