n = 7
apart = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1],
         [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 0]]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# n = int(input())
# apart = []

# for _ in range(n):
#   apart.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False

    if apart[x][y] == 1:
        apart[x][y] = apart_num
        if len(house_holds) < apart_num - 1:
            house_holds.append(1)
        else:
            house_holds[apart_num - 2] += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


house_holds = []
apart_num = 2
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            apart_num += 1

house_holds.sort()
print(len(house_holds))
for house in house_holds:
    print(house)
