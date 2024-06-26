import heapq
import sys
input = sys.stdin.readline
n = int(input())

heap = []

for _ in range(n):
  i = int(input())
  if(i == 0):
    if(len(heap) == 0): print(0)
    else:
      out = heapq.heappop(heap)
      print(out)
  else: heapq.heappush(heap,i)