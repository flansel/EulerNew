from itertools import permutations

d = ["9","8","7","6","5","4","3","2","1","0"]
l = permutations(d)

ans = 0

for x in l:
    s = "".join(x)
    if int(s[1:4]) % 2 != 0:
        continue
    if int(s[2:5]) % 3 != 0:
        continue
    if int(s[3:6]) % 5 != 0:
        continue
    if int(s[4:7]) % 7 != 0:
        continue
    if int(s[5:8]) % 11 != 0:
        continue
    if int(s[6:9]) % 13 != 0:
        continue
    if int(s[7:10]) % 17 != 0:
        continue
    ans += int(s)
print(ans)
