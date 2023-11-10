import heapq
import sys

readline = sys.stdin.readline

n, c = 6, 60
m = 5
num = [[1, 2, 30], [2, 5, 70], [5, 6, 60], [3, 4, 40], [1, 6, 40]]

num.sort()
print(num)

queue = []

for start, end, weight in num:
    if (weight < c):
        heapq.heappush(queue, weight)
    if (start < len(queue)):
        heapq.heappop(queue)
    print(queue)

print(sum(queue))