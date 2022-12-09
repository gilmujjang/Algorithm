import sys
import heapq
input = sys.stdin.readline

n, k = 3, 2

gems = [[1, 65], [5, 23], [2, 99]]
bags = [10, 2]

# n, k = map(int, input().split())
# gems = [list(map(int, input().split())) for _ in range(n)]
# bags = [int(input()) for _ in range(k)]

gems.sort()
bags.sort()

queue = []
money = 0

for bag in bags:
    while gems and bag >= gems[0][0]:
        heapq.heappush(queue, -gems[0][1])
        heapq.heappop(gems)
    if queue:
        money += heapq.heappop(queue)
print(-money)