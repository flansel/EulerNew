import math
import feuler

n = 600851475143

#print(feuler.isPrime(60))
#print(feuler.isPrime(17))

for i in range(int(math.sqrt(n)),1,-1):
    if n % i == 0 and feuler.miller_rabin(i):
        print(i)
        break

print("done")        
