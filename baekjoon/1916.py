from heapq import heappush, heappop

inf = 100001
v, e = 5, 8
li = [
    "1 2 2", "1 3 3", "1 4 1", "1 5 10", "2 4 2", "3 4 1", "3 5 1", "4 5 3",
    "1 5"
]
start, end = map(int, li[e].split())

s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []


def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        for n_n, wei in s[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])


for i in range(e):
    u, v, w = map(int, li[i].split())
    s[u].append([v, w])

dijkstra(start)
print(dp[end])