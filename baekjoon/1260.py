from sys import stdin
a, b, n = map(int, stdin.readline().split())

# a = 5
# b = 5
# n = 3

# py = ["5 4", "5 2", "1 2", "3 4", "3 1"]

dfs_node = [[False for _ in range(a)] for _ in range(a)]
bfs_node = [[False for _ in range(a)] for _ in range(a)]
for i in range(b):
    x, y = map(int, stdin.readline().split())
    # x, y = map(int, py[i].split())
    dfs_node[x - 1][y - 1] = True
    dfs_node[y - 1][x - 1] = True
    bfs_node[x - 1][y - 1] = True
    bfs_node[y - 1][x - 1] = True

visit_dfs = []
visit_bfs = []


def dfs(n):
    visit_dfs.append(n)
    for i in range(a):
        if dfs_node[n - 1][i] == True:
            if i + 1 not in visit_dfs:
                dfs_node[n - 1][i] = False
                dfs_node[i][n - 1] = False
                dfs(i + 1)


def bfs(n):
    golist = [n]
    while golist:
        start = golist.pop(0)
        visit_bfs.append(start)
        for i in range(a):
            if bfs_node[start - 1][i] == True:
                if i + 1 not in visit_bfs:
                    if i + 1 not in golist:
                        bfs_node[start - 1][i] = False
                        bfs_node[i][start - 1] = False
                        golist.append(i + 1)


dfs(n)
bfs(n)
print(" ".join(map(str, visit_dfs)))
print(" ".join(map(str, visit_bfs)))
