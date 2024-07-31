import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

maxValue = 0

def dfs(x, y, value, cnt):
  global maxValue
  if(cnt == 4):
    maxValue = max(maxValue, value)
    return
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if( nx < 0 or nx >= M or ny < 0 or ny >= N or visited[ny][nx]):
      continue
    visited[ny][nx] = True
    dfs(nx, ny, value + graph[ny][nx], cnt + 1)
    visited[ny][nx] = False

def etc(x, y):
  global maxValue
  array = []
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx < 0 or nx >= M or ny < 0 or ny >= N):
      continue
    array.append(graph[ny][nx])
  if(len(array) == 4):
    array.sort(reverse=True)
    array.pop()
    maxValue = max(maxValue, sum(array) + graph[y][x])
  elif(len(array) == 3):
    maxValue = max(maxValue, sum(array) + graph[y][x])
  return

for i in range(N):
  for j in range(M):
    visited[i][j] = True
    dfs(j, i, graph[i][j], 1)
    etc(j, i)
    visited[i][j] = False

print(maxValue)