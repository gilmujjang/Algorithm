import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
  num = int(input())
  if(num == 0): queue.pop()
  else: queue.append(num)

print(sum(queue))