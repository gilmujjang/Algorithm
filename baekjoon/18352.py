from heapq import heappush, heappop

inf = 300001
v,e,target,start = 4,3,2,1
li = ["1 2","1 3","1 4"]

s = [[] for _ in range(v+1)]
dp = [inf]*(v+1)
heap = []
result = []

def dijkstra(start):
  dp[start] = 0
  heappush(heap, [0, start])
  while heap:
    w, n = heappop(heap)
    for n_n, wei in s[n]:
      n_w = wei + w
      if n_w < dp[n_n]:
        dp[n_n] = n_w
        heappush(heap, [n_w, n_n])
      


for i in range(e):
  u,v = map(int,li[i].split())
  w=1
  s[u].append([v,w])
dijkstra(start)
for i in range (len(dp)):
  if(dp[i]==target):
    result.append(i)

if not result:
  print(-1)
  
for i in result:
  print(i)

