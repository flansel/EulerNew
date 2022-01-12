f = open("tri_num.txt", "r")

s = f.read().replace("\"", "").replace("\n", "").split(",")

ans = 0
tri = []

for i in range(100):
    tri.append(int(.5*i*(i+1)))
print(tri)
for w in s:
    m = 0
    for c in w:
        m += (ord(c) - ord("A"))+1
    if m in tri:
        ans += 1

print(ans)
