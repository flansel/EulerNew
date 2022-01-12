s = ""

for i in range(1,500000):
    s += str(i)

print(int(s[1-1]) * int(s[10-1]) * int(s[100-1]) * int(s[1000-1]) * int(s[10000-1]) * int(s[100000-1]) * int(s[1000000-1]))
