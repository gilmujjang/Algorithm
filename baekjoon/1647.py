n = 7
m = 12
li = ["1 2 3","1 3 2","3 2 1","2 5 2","3 4 4","7 3 6","5 1 5","1 6 2","6 4 1","6 5 3","4 5 3","6 7 4"]
from sys import stdin
#n,m = map(int, stdin.readline().split())

arr = []
ans = 0
parent = [i for i in range(0, n+1)]
weight = 0
node = 0

for i in range(m):
  arr.append(list(map(int, li[i].split())))
  #arr.append(list(map(int,stdin.readline().split())))
arr = sorted(arr, key=lambda k: k[2])

def find(x):
  if x==parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  x,y = find(x),find(y)
  if x != y:
    parent[y] = x

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
print(ans)
print(weight)
print(ans-weight)