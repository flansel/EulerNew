it = 0
ans = 0

def is_pal(N):
    if str(N) == str(N)[::-1]:
        return True
    return False

for i in range(0, 10001):
    x = int(str(i)[::-1])
    x += i
    it = 1
    while True:
        #print(x,i,it)
        if is_pal(x):
            break
        it += 1
        if it > 50:
            print(i)
            ans += 1
            break
        r = int(str(x)[::-1])
        x += r
print(ans)
