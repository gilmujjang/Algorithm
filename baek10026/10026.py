#n = 5
#example = ["RRRBB","GGBBB","BBBRR","BBRRR","RRRRR"]
from sys import stdin

n = int(stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
normal = []
colorLess = [[0]*n for _ in range(n)]
norm = 0
less = 0

for i in range(n):
  normal.append(list(stdin.readline()))

for i in range(n):
  for j in range(n):
    if normal[i][j] == "R":
      colorLess[i][j] = "R"
    elif normal[i][j] == "G":
      colorLess[i][j] = "R"
    elif normal[i][j] == "B":
      colorLess[i][j] = "B"

def bfs_normal(color, i, j):
  queue = [[i,j]]
  normal[i][j] = 0
  while queue:
    for _ in range(len(queue)):
      x,y = queue[0][0],queue[0][1]
      del queue[0]
      for i in range(4):
        q = x + dx[i]
        w = y + dy[i]
        if 0 <= q < n and 0 <= w < n and normal[q][w]==color:
          normal[q][w] = 0
          queue.append([q,w])

def bfs_colorLess(color, i, j):
  queue = [[i,j]]
  while queue:
    for _ in range(len(queue)):
      x, y = queue[0][0], queue[0][1]
      del queue[0]
      for i in range(4):
        q = x + dx[i]
        w = y + dy[i]
        if 0 <= q < n and 0 <= w < n and colorLess[q][w]==color:
          colorLess[q][w] = 0
          queue.append([q,w])

for i in range(n):
  for j in range(n):
    if normal[i][j] != 0:
      norm += 1
      bfs_normal(normal[i][j],i,j)

for i in range(n):
  for j in range(n):
    if colorLess[i][j] != 0:
      less += 1
      bfs_colorLess(colorLess[i][j],i,j)

print(norm," ",less)
