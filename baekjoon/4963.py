from sys import stdin

dx = [1, 1, 0, -1, -1, -1,  0,  1]
dy = [0, 1, 1,  1,  0, -1, -1, -1]

def bfs(x, y):
  queue = [[x, y]]
  land[x][y]==0
  while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(8):
      q = a + dx[i]
      w = b + dy[i]
      if 0 <= q < n and 0 <= w < m and land[q][w] == 1:
        land[q][w] = 0
        queue.append([q, w])

while True:
  count = 0
  m,n = map(int,stdin.readline().split())
  if m==0 and n==0:
    break
  land = []
  for i in range(n):
    land.append(list(map(int,stdin.readline().split())))
  for i in range (n):
    for j in range(m):
      if land[i][j]==1:
        bfs(i,j)
        count +=1

  print(count)
