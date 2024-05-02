import sys

input = sys.stdin.readline

# x, y = [3, 3]
# blocks = [[1, 3, 4],
#           [2, 2, 3],
#           [1, 2, 4]]
x, y = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(x)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

for i in range(x):
  for j in range(y):
    height = blocks[i][j]
    if(height != 0):
      temp = 6 * height - 2 * (height - 1)
      for k in range(4):
        if i-dx[k] >= 0 and i-dx[k] <= x-1 and j-dy[k] >= 0 and j-dy[k]<=y-1:
          temp -= min(height, blocks[i-dx[k]][j-dy[k]])
      count += temp

print(count)
