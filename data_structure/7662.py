import sys
import heapq

input = sys.stdin.readline
n = int(input())

def isEmpty(storage):
  for item in storage:
    if(item[1]> 0):
      return False
  return True

def func():
  m = int(input())
  min_heap = []
  max_heap = []
  storage = dict()
  for _ in range(m):
    command, number = input().split()
    number = int(number)
    if(command == 'I'):
      if(number in storage):
        storage[number] += 1
      else:
        storage[number] = 1
        heapq.heappush(min_heap, number)
        heapq.heappush(max_heap, -number)
    if(command == 'D'):
      if not isEmpty(storage.items()):
        if(number == 1):
          while -max_heap[0] not in storage or storage[-max_heap[0]] < 1:
            temp = -heapq.heappop(max_heap)
            if(temp in storage):
              del(storage[temp])
          storage[-max_heap[0]] -= 1
        else:
          while min_heap[0] not in storage or storage[min_heap[0]] < 1:
            temp = heapq.heappop(min_heap)
            if(temp in storage):
              del(storage[temp])
          storage[min_heap[0]] -= 1
        

  if(isEmpty(storage.items())):
    print('EMPTY')
  else:
    while min_heap[0] not in storage or storage[min_heap[0]] < 1:
      heapq.heappop(min_heap)
    while -max_heap[0] not in storage or storage[-max_heap[0]] < 1:
      heapq.heappop(max_heap)
    print(-max_heap[0], min_heap[0])

for _ in range(n):
  func()