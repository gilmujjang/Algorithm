#n = 5
#example = ["6 8 2 6 2","3 2 3 4 6","6 7 3 3 2","7 2 5 3 6","8 9 5 2 7"]
from sys import stdin

n = int(stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
li = []
safelist = []

for i in range(n):
  li.append(list(map(int,stdin.readline().split())))

def bfs(i,j):
  queue = [[i,j]]
  while queue:
    for _ in range (len(queue)):
      a, b = queue[0][0],queue[0][1]
      del queue[0]
      for i in range(4):
        q = a + dx[i]
        w = b + dy[i]
        if 0 <= q < n and 0 <= w < n and virtualLand[q][w]==1:
          virtualLand[q][w] = 0
          queue.append([q, w])

for h in range(max(map(max, li))):
  virtualLand = [[0]*n for _ in range(n)]
  safe = 0
  #복사본 생성
  for i in range(n):
    for j in range(n):
      if li[i][j] > h:
        virtualLand[i][j] = 1
  # 탐색
  for i in range(n):
    for j in range(n):
      if virtualLand[i][j] == 1:
        safe += 1
        virtualLand[i][j] = 0
        bfs(i,j)
  if safe == 0:
    break

  safelist.append(safe)

print(max(safelist))