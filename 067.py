f = open("067_triangle.txt", "r")
s = f.read()
a = s.split("\n")
for i in range(len(a)-1):
    a[i] = a[i].split(" ")
    for j in range(len(a[i])):
        a[i][j] = int(a[i][j])
a.pop()

for i in range(len(a)-2,-1,-1):
    for j in range(len(a[i])):
        a[i][j] += a[i+1][j] if a[i+1][j] > a[i+1][j+1] else a[i+1][j+1]
print(a[0][0])
