import heapq
import sys

readline = sys.stdin.readline

n = 7
num = [[1, 6], [1, 7], [3, 2], [3, 1], [2, 4], [2, 5], [6, 1]]

n = int(input())
num = []
# for _ in range(n):
#     deadline, noodle = map(int, readline().strip("\n").split())
#     num.append([deadline, noodle])

num.sort()

queue = []
for deadline, noodle in num:
    heapq.heappush(queue, noodle)
    if (deadline < len(queue)):
        heapq.heappop(queue)
print(sum(queue))
