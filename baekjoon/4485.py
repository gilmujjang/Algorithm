from heapq import heappush, heappop

dx = [1,-1,0,0]
dy = [0,0,1,-1]
inf = 1000000000

def Dijkstra(cnt):
  dp = [[inf]*n for _ in range(n)]
  heap = []
  heappush(heap,[cave[0][0],0,0])
  dp[0][0] = 0

  while heap:
    w,x,y = heappop(heap)
    if x == n-1 and y == n-1:
      print("Problem {0}: {1}".format(cnt,w))
      return
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        nw = w + cave[nx][ny]
        if nw < dp[nx][ny]:
          dp[nx][ny] = nw
          heappush(heap,[nw, nx, ny])
          
      
cnt = 1
while True:
  n = int(input())
  if n == 0:
    break
  cave = [list(map(int,input().split())) for _ in range(n)]
  Dijkstra(cnt)
  cnt += 1