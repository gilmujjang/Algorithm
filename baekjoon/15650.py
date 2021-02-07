#N, M = map(int, input().split())
n,m = 6, 3
visited = [False] * n
result = []

def solve(depth, x, n, m):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(x, n):
        if not visited[i]:
            visited[i] = True
            result.append(i+1)
            solve(depth+1, i+1, n, m)
            visited[i] = False
            result.pop()
solve(0, 0, n, m)
