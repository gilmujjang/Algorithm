from collections import deque

node_num = 7
edge_num = 6
computers = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]

graph = [[] for _ in range(node_num + 1)]

node_num = int(input())
edge_num = int(input())
computers = []
for _ in range(m):
    computers.append(list(map(int, input().split())))

for edge in computers:
    start, end = map(int, edge)
    graph[start].append(end)
    graph[end].append(start)

visited = [False] * (node_num + 1)


def bfs(start):
    queue = deque([start])
    visited[start] = True
    virus = -1
    while queue:
        next_infect = queue.popleft()
        virus += 1
        for i in graph[next_infect]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return virus


print(bfs(1))
