from heapq import heappush, heappop

inf = 100000
start, end = 1, 2
v, e = 4, 4

li = ['1 3', '1 4', '3 2', '4 2']

s = [[] for _ in range(v + 1)]
dp = [inf] * (v + 1)
heap = []


def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        print(heap)
        for n_n in s[n]:
            n_w = 1 + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
                print(heap)


for i in range(e):
    u, v = map(int, li[i].split())
    s[u].append(v)
    s[v].append(u)

dijkstra(start)
if (dp[end] < inf):
    print(dp[end])
else:
    print(-1)
print(dp)