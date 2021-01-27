from sys import stdin

def find(x):
  if x==parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  x,y = find(x),find(y)
  if x != y:
    parent[y] = x

while True:
  n,m = map(int, stdin.readline().split())
  if(n,m) == (0,0):
    break
  ans = 0
  parent = [i for i in range(n)]
  weight = 0
  node = 0
  arr = []
  su = 0
  for i in range(m):
    a,b,c = map(int, stdin.readline().split())
    arr.append([a,b,c])
    su = su + c
  arr = sorted(arr, key=lambda k: k[2])

  for i in arr:
    start, end, weight = i
    if find(start) == find(end):
      continue
    else:
      ans += weight
      union(start,end)
      node += 1
    if node == n-1:
      break

  print(su-ans)