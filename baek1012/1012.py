
#https://pacific-ocean.tistory.com/270 베껴옴
from sys import stdin

t = int(stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and farm[q][w] == 1:
                farm[q][w] = 0
                queue.append([q, w])

for i in range(t):
    m, n, k = map(int, stdin.readline().split())
    farm = [[0] * m for i in range(n)]
    bug = 0

    for j in range(k):
        x, y = map(int, stdin.readline().split())
        farm[y][x] = 1

    for q in range(n):
        for w in range(m):
            if farm[q][w] == 1:
                bfs(q, w)
                farm[q][w] = 0
                bug += 1
    print(bug)