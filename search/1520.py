import sys
m, n = map(int, input().split())
navi = [list(map(int, input().split())) for _ in range(m)]
sys.setrecursionlimit(10**6)
# m, n = 4, 5
# navi = [[50, 45, 37, 32, 30], [35, 50, 40, 20, 25], [30, 30, 25, 17, 28],
#         [27, 24, 22, 15, 10]]

dp = [[-1] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if navi[x][y] > navi[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]


print(dfs(0, 0))
