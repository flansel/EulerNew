import math

def is_prime(N):
    if N < 2:
        return False
    
    for i in range(2,int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

c_streak = 0
m_streak = [0,0,0]
n = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        while is_prime(n**2 + a*n + b):
            #print(a, b, n)
            c_streak+=1
            n+=1
        print(a,b,m_streak)
        if c_streak > m_streak[0]:
            m_streak[0] = c_streak
            m_streak[1] = a
            m_streak[2] = b
        c_streak = 0
        n = 0
print(m_streak, a, b, a*b)
