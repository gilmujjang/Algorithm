a = 4
b = 6
example = ["101111","101010","101011","111011"]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
li = []

for i in range (a):
  li.append(list(example[i]))

visited = [[0,0]]
while visited:
  q,w = visited[0][0], visited[0][1]
  del visited[0]
  for i in range(4):
    x = q + dx[i]
    y = w + dy[i]
    if 0 <= x < a and 0 <= y < b and li[x][y]=="1":
      visited.append([x,y])
      li[x][y] = int(li[q][w]) + 1
print(li)
print(li[a-1][b-1])

# from sys import stdin

# a,b = map(int, stdin.readline().split())
# dx = [1, -1, 0, 0]
# dy = [0, 0, -1, 1]
# visited = [[0,0]]
# li = []

# for _ in range (a):
#   li.append(list(stdin.readline()))

# li[0][0] = 1
# while visited:
#   q,w = visited[0][0], visited[0][1]
#   del visited[0]
#   for i in range(4):
#     x = q + dx[i]
#     y = w + dy[i]
#     if 0 <= x < a and 0 <= y < b and li[x][y]=="1":
#       visited.append([x,y])
#       li[x][y] = li[q][w] + 1

# print(li[a-1][b-1])