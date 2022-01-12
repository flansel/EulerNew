import math

def is_prime(N):
    if N < 2:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def rtp(N):
    while N > 0:
        #print(N)
        if is_prime(N) == False:
            return False
        N = int(N/10)
    return True

def ltp(N):
    N = str(N)
    while N != "":
        if is_prime(int(N)) == False:
            return False
        N = N[1:]
    return True

tc = 0
s = 0
i = 10

#print(rtp(3797))
#print(ltp(3797))

while tc < 11:
    for x in list(str(i)):
        if int(x) % 2 == 0:
            i+=1
            break
    if rtp(i) == True and ltp(i) == True:
        tc += 1
        s += i
        print(i)
    i+=1
print(s)
