# from sys import stdin
 #num = int,stdin.readline().split()

 #row, column, n = map(int,stdin.readline().split())
row = 10
column = 8
n = 17

# 1 1 0 0 0 0 0 0 0 0
# 0 1 0 0 0 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 0 0 1 0 0 0 0 0
# 0 0 1 1 0 0 0 1 1 1
# 0 0 0 0 1 0 0 1 1 1
# 0 0 0 0 0 0 0 1 1 1
# 0 0 0 0 0 0 0 0 0 0


li = ["0 0", "1 0", "1 1", "4 2", "4 3", "4 5", "2 4", "3 4", "7 4", "8 4", "9 4", "7 5", "8 5", "9 5", "7 6", "8 6", "9 6"]

node = [[0 for row in range(row)] for column in range(column)]

for i in range (n):
  y,x = map(int, li[i].split())
  node[x][y] = 1

bug = 0

def bug_move(r,c):
  golist = [r,c]
  alreadyeat = []
  while golist:
    start = golist.pop(0)
    alreadyeat.append(start)
    if c != 0 :  # 왼쪽으로 한칸
      if node[r][c-1] == 1 :
        if node[r][c-1] not in alreadyeat :
          if node[r][c-1] not in golist :
            node[r][c-1] = 0
            golist.append([r,c-1])

    if c != column-1 :  # 오른쪽으로 한칸
      if node[r][c+1] == 1 :
        if node[r][c+1] not in alreadyeat :
          if node[r][c+1] not in golist :
            node[r][c+1] = 0
            golist.append(node[r][c+1])

    if r != 0 :  # 위쪽으로 한칸
      if node[r-1][c] == 1 :
        if node[r-1][c] not in alreadyeat :
          if node[r-1][c] not in golist :
            node[r-1][c] = 0
            golist.append(node[r-1][c])

    if r != row-1 :  # 아래쪽으로 한칸
      if node[r+1][c] == 1 :
        if node[r+1][c] not in alreadyeat :
          if node[r+1][c] not in golist :
            node[r+1][c] = 0
            golist.append(node[r+1][c])


for r in range (10):
  for c in range (8):
    print(node[c][r])
    if node[c][r] == 1:
      bug = bug +1
      bug_move(c,r)
    