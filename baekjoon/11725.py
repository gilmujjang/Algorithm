from sys import stdin

n = int(stdin.readline())
#n = 7
#example = ["1 6","6 3","3 5","4 1","2 4","4 7"]

node = [[] for _ in range(n+1)]
parent = [[] for _ in range(n+1)]

for _ in range (n-1):
  #x,y = map(int,example[i].split())
  x,y = map(int,stdin.readline().split())
  node[x].append(y)
  node[y].append(x)

def dfs(graph):
  stack = [1]
  while stack:
    ascendent = stack.pop()
    for i in graph[ascendent]:
      parent[i].append(ascendent)
      stack.append(i)
      graph[i].remove(ascendent)

dfs(node)

for i in range(len(parent)-2):
  print(parent[i+2][0])
