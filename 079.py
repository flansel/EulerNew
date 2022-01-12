f = open("079_keylog.txt", "r")

j = [[] for i in range(10)]

for l in f:
    j[int(l[2])].append(int(l[1]))
    j[int(l[2])].append(int(l[0]))
    j[int(l[1])].append(int(l[0]))

for i,r in enumerate(j):
    print(i, ":", set(r))

