import math
import feuler

def solve():
    ans = 0
    for i in range(999, 0, -1):
        for j in range(999, 0, -1):
            m = i*j
            n = str(i*j)
            if n == n[::-1]:
                ans = m if m > ans else ans
    return ans         
print(solve())
print("done")
