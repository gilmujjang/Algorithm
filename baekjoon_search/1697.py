from collections import deque

# n, m = map(int, input().split())

n, m = 65432, 99999
max = 100000


def bfs(position):
    count = 0
    visited = [False] * (max + 1)
    queue = deque([[position, count]])
    while queue:
        subin = queue.popleft()
        position = subin[0]
        count = subin[1]
        if not visited[position]:
            visited[position] = count
            if position == m:
                print(count)
                return
            count += 1
            if 0 <= (position * 2) <= max:
                queue.append([position * 2, count])
            if 0 <= (position + 1) <= max:
                queue.append([position + 1, count])
            if 0 <= (position - 1) >= 0:
                queue.append([position - 1, count])


bfs(n)