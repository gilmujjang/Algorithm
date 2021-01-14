# a = 6
# b = 5
# li = ["1 2","2 5","5 1","3 4","4 6"]

from sys import stdin

a,b = map(int, stdin.readline().split())

node = [[] for _ in range(a+1)]
visited = [False]*(a+1)
ans = 0

for i in range(b):
  x,y = map(int, stdin.readline().split())
  node[x].append(y)
  node[y].append(x)

def bfs(start):
  queue = [start]
  while queue:
    start = queue.pop(0)
    for i in node[start]:
      if visited[i] == False:
        queue.append(i)
        visited[i] = True

for i in range(1,a+1):
  if visited[i] == False:
    bfs(i)
    ans += 1

print(ans)