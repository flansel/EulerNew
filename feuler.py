import math
import random
die = random.SystemRandom() # A single dice.
import time

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def single_test(n, a):
    exp = n - 1
    while not exp & 1:
        exp >>= 1
        
    if pow(a, exp, n) == 1:
        return True
        
    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True
        exp <<= 1    
    return False
    
def miller_rabin(n, k=40):
    for i in range(k):
        a = die.randrange(2, n - 1)
        if not single_test(n, a):
            return False            
    return True

def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    ptrack = 0
    for idx in range(2, len(a)):
        if a[idx] == False:
            continue
        x = idx*2
        while x < len(a):
            a[x] = False
            x+=idx
    return a

