import math

su = [[[],[],[3],[],[2],[],[6],[],[]],
      [[9],[],[],[3],[],[5],[],[],[1]],
      [[],[],[1],[8],[],[6],[4],[],[]],
      [[],[],[8],[1],[],[2],[9],[],[]],
      [[7],[],[],[],[],[],[],[],[8]],
      [[],[],[6],[7],[],[8],[2],[],[]],
      [[],[],[2],[6],[],[9],[5],[],[]],
      [[8],[],[],[2],[],[3],[],[],[9]],
      [[],[],[5],[],[1],[],[3],[],[]]]

rows = []
cols = []

for row in su:
    for col in row:
        if len(su[row][col]) == 1:
            su[row][col] = list(range(1,10))
for row in su:
    rows.append(find_row(row))
    for col in row:
        cols.append(find_col(col))
