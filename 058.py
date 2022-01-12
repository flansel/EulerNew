import math
import f_utils

def is_prime(N):
    if N < 2:
        return False
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

n = 1
sd = 1
pc = 0
inc = 2

while sd < 7 or pc/((2*sd)-1) > .1:
    for i in range(4):
        #print(n, is_prime(n))
        n += inc
        if is_prime(n) == True:
            pc += 1
    inc += 2
    sd += 2
print(sd, inc, pc, pc/(2*sd-1))
