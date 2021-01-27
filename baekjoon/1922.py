from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

arr = []
for i in range(m):
  arr.append(list(map(int,stdin.readline().split())))
#비용별로 정렬
arr = sorted(arr, key=lambda k: k[2])

parent = [i for i in range(0,n+1)]
ans = 0

def find(x):
  if x==parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  x,y = find(x),find(y)
  parent[x] = y

for i in arr:
  start, end, weight = i
  if find(start) == find(end):
    continue
  else:
    ans += weight
    union(start,end)

print(ans)