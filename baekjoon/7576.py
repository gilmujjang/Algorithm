from sys import stdin
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  days = 0
  while queue:
    days += 1
    for _ in range (len(queue)):
      a, b = queue.popleft()
      for i in range(4):
        q = a + dx[i]
        w = b + dy[i]
        if 0 <= q < n and 0 <= w < m and li[q][w] == 0:
          li[q][w] = 1
          queue.append([q, w])
  return days

m,n = map(int,stdin.readline().split())
li,queue = [], deque()

for i in range(n):
  a = list(map(int,stdin.readline().split()))
  for j in range(m):
    if a[j] == 1 :
      queue.append([i,j])
  li.append(a)

days = bfs() -1

for i in range (n):
  for j in range (m):
    if li[i][j] == 0:
      print(-1)
      exit()

print(days)