# n = 9
# a = 7
# b = 3
# no = 7
# li = ["1 2","1 3","2 7","2 8","2 9","4 5","4 6"]
from sys import stdin
from collections import deque

n = int(stdin.readline())
a,b = map(int, stdin.readline().split())
no = int(stdin.readline())

node = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(no):
  x, y = map(int, stdin.readline().split())
  node[x].append(y)
  node[y].append(x)

def bfs(a,b):
  chon = 0
  queue = deque([[a, chon]])
  while queue:
    x = queue.popleft()
    a = x[0]
    chon = x[1]
    if a == b:
      print(chon)
      exit()
    if not visited[a]:
      chon += 1
      visited[a] = True
      for i in node[a]:
        if not visited[i]:
          queue.append([i, chon])
  print(-1)

bfs(a,b)

