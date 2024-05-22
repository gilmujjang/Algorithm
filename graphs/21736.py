import sys
from collections import deque 

input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
person = 0

# O 는 빈공간
# X 는 벽
# I 는 나
# P 는 사람

dx, dy = [0,0,-1,1], [-1,1,0,0]

def bfs(i, j):
  global person
  queue = deque()
  queue.append((i, j))
  visited[i][j] = True
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if(0<=nx<N and 0<=ny<M and campus[nx][ny] != 'X' and visited[nx][ny] == False):
        if(campus[nx][ny] == 'P'): person += 1
        visited[nx][ny] = True
        queue.append((nx, ny))

for i in range(N):
  for j in range(M):
    if(campus[i][j] == 'I'): bfs(i, j)

print('TT' if person == 0 else person)