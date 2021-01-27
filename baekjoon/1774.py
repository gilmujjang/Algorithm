
li = ["4 1","1 1","3 1","2 3","4 3","1 4"]

arr = []

n,m = map(int, li.pop(0).split())
location = list(map(int, li[0].split()))
parent = [i for i in range(n+1)]
dis = 0
node = 0
arr = []

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
  distance = ((x-location[0])**2 + (y-location[1])**2)**0.5
  arr.append([x,y,round(distance,2)])

path = list(map(int, li[0].split()))
union(path[0],path[1])

arr = sorted(arr, key=lambda k: k[2])
print(arr)

for i in arr:
    start, end, distance = i
    if find(start) == find(end):
      continue
    else:
      dis += distance
      union(start,end)
      node += 1
    if node == n-1:
      break

print(dis)