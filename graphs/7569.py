import sys
from collections import deque 
import itertools

input = sys.stdin.readline

N, M, H = map(int, input().split())
box = [list(list(map(int, input().split())) for _ in range(M)) for _ in range(H)]
days = -1

dx, dy, dz = [0,0,0,0,-1,1], [0,0,-1,1,0,0], [-1,1,0,0,0,0]


def bfs(queue):
  global days
  while True:
    if(len(queue) == 0): break
    else:
      days += 1
      for _ in range(len(queue)):
        z,y,x = queue.popleft()
        for i in range(6):
          nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
          if(0<=nx<N and 0<=ny<M and 0<=nz<H and box[nz][ny][nx] == 0):
            box[nz][ny][nx] = 1
            queue.append((nz, ny, nx))

queue = deque()
for h in range(H):
  for m in range(M):
    for n in range(N):
      if(box[h][m][n] == 1): queue.append((h,m,n))

bfs(queue)

flatten_list = list(itertools.chain(*list(itertools.chain(*box))))
print(-1 if 0 in flatten_list else days)


