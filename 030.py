s = 0

for i in range(2,(9**5 * 5)+1):
    n = i
    t = 0
    while n > 10:
        t+=(n%10)**5
        n//=10
    t+=(n%10)**5
    if t == i:
        s+=i
        print(i)
print(s)
