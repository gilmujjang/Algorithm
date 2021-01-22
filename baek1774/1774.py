
li = ["4 1","1 1","3 1","2 3","4 3","1 4"]

arr = []
dist = []

n,m = map(int, li.pop(0).split())
location = list(map(int, li[0].split()))
parent = [i for i in range(n+1)]
dis = 0
node = 0
ans = 0

def find(x):
  if x==parent[x]:
    return x
  parent[x] = find(parent[x])
  return parent[x]

def union(x,y):
  x,y = find(x),find(y)
  if x != y:
    parent[y] = x

for i in range(n):
  x, y = map(int, li.pop(0).split())
  arr.append([x,y])

print(li)

for i in range(n+1):
  for j in range(n+1):
    if i != j:
      x,y = arr[i]
      a,b = arr[j]
      distance = ((x-a)**2 + (y-b)**2)**0.5
      dist.append([i,j,distance])

dist = sorted(dist, key=lambda k: k[2])
print(dist)
union(n,m-1)
for i in dist:
    start, end, weigh = i
    if find(start) == find(end):
      continue
    else:
      union(start,end)
      node += 1
      print(weigh)
      ans += weigh
    if node == n-1:
      break

print(ans)
print(parent)