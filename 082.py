f = open("082matrix.txt", "r")

mtx = f.read().split("\n")
mtx.pop()

for i,row in enumerate(mtx):
    mtx[i] = row.split(",")
    for j,n in enumerate(mtx[i]):
        mtx[i][j] = int(n)
#    mtx[i].append(0)

local = [0 for i in range(len(mtx))]

tst = [[131, 673, 234, 103, 18],
        [201, 96, 342, 965, 150],
        [630, 803, 746, 422, 111],
        [537, 699, 497, 121, 956],
        [805, 732, 524, 37, 331]]


def dj(matrix, start):
    visited = [[False for i in range(len(matrix)+1)] for j in range(len(matrix)+1)]
    tdist = [[1000000000 for i in range(len(matrix)+1)] for j in range(len(matrix)+1)]

    unvisited = {}
    for i in range(len(matrix)+1):
        for j in range(len(matrix)+1):
            unvisited[(i,j)] = 1000000000


    tdist[start[0]][start[1]] = 0
    curr = start

    offsets = [(-1,0),(1,0),(0,1)]

    while len(unvisited) > 0:
        #print(curr, unvisited[curr], "d")
        visited[curr[0]][curr[1]] = True

        if curr == (len(matrix),len(matrix)):
            break
        for (rowoff, coloff) in offsets:
            if curr[0] + rowoff < 0 or curr[0] + rowoff > len(matrix) - 1:
                continue
            if curr[1] + coloff < 0 or curr[1] + coloff > len(matrix) - 1:
                continue

            r = curr[0] + rowoff
            c = curr[1] + coloff

            if visited[r][c] == False:
                x = min(tdist[r][c], tdist[curr[0]][curr[1]] + matrix[curr[0]][curr[1]])
                tdist[r][c] = x
                unvisited[(r,c)] = x
        unvisited.pop(curr, None)
        curr = min(unvisited, key=unvisited.get)
    return tdist

mn = 100000000000
tst = mtx
for k in range(len(tst)):
    x = dj(tst,(k,0))
    print(k)
    for i in range(len(x)-1):
        x[i][len(tst)]  = x[i][len(tst)-1] + tst[i][len(tst)-1]
        if x[i][len(tst)] < mn:
            mn  = x[i][len(tst)]
    

print(mn)





































