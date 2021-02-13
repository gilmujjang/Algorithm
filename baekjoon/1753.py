#from sys import stdin
import heapq
import sys

inpu = ["5 1 1","1 2 2","1 3 3","2 3 4","2 4 5","3 4 6"]
INF = sys.maxsize
#v,e = map(int,stdin.readline.split())
v, e = 5, 6
#k = int(stdin.readline())
k = 2
dp = [INF]*(v+1)
heap = []
graph = [[] for _ in range(v + 1)]

def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:
            continue
        for w, next_node in graph[now]:
            next_wei = w + wei
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))

for i in range(e):
    #a,b,c = map(int, stdin.readline().split())
    a,b,c = map(int, inpu[i].split())
    graph[a].append((c,b))

dijkstra(k)
for i in range(1, v+1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
