curr = 0
m = 0

for i in range(1, 100):
    for j in range(1, 100):
        curr = 0
        x = list(str(i**j))
        for d in x:
            curr += int(d)
        if curr > m:
            m = curr
print(m)
