f = open("matrix.txt", "r")

def cnv(N):
    return int(N)

mtx = [list(map(cnv, f.readline().split(","))) for i in range(80)]

for i in reversed(range(80)):
    for j in reversed(range(80)):
        if i == 79 and j == 79:
            pass
        elif i ==79:
            mtx[i][j] += mtx[i][j+1]
        elif j == 79:
            mtx[i][j] += mtx[i+1][j]
        else:
            mtx[i][j] += min(mtx[i+1][j],mtx[i][j+1])
print(mtx[0][0])
