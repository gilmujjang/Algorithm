# n = 7
# m = 8
# li = ["0 1 3","1 1 7","0 7 6","1 7 1","0 3 7","0 4 2","0 1 1","1 1 1"]
from sys import stdin

n,m = map(int, stdin.readline().split())

parent = [i for i in range(n+1)]
def find(id):
  if(parent[id] == id):
    return id
  #parent[id] = find(parent[id])
  return parent[id]

def check(a,b):
  if find(a) == find(b):
    return True
  else:
    return False

def union(a,b):
  ca = find(a)
  cb = find(b)
  if not ca == cb:
    parent[cb] = ca


for i in range(m):
  f,a,b = map(int,stdin.readline().split())
  if f:
    if check(a,b):
      print("YES")
    else:
      print("NO")
  else:
    union(a,b)
