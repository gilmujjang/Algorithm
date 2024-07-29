import sys
from collections import deque 

input = sys.stdin.readline

N = int(input())
MAX = 10000

def converter(data, command):
  if(command == 'D'):
    result = data*2
    return result if result < MAX else result-MAX
  elif(command == 'S'):
    result = data-1
    return result if result >= 0 else MAX-1
  elif(command == 'L'):
    result = 10*data
    return result if result < MAX else result%MAX  + result//MAX
  elif(command == 'R'):
    result = data // 10
    return result if data%10 == 0 else result + (data%10)*1000

for _ in range(N):
  start, end = map(int, input().split())
  queue = deque()
  visited = set()
  queue.append((start, ""))
  visited.add(start)
  while queue:
    target, command = queue.popleft()
    if(target == end):
      print(command)
      break
    D = converter(target, 'D')
    S = converter(target, 'S')
    L = converter(target, 'L')
    R = converter(target, 'R')
    if(D not in visited):
      visited.add(D)
      queue.append((D, command + "D"))
    if(S not in visited):
      visited.add(S)
      queue.append((S, command + "S"))
    if(L not in visited):
      visited.add(L)
      queue.append((L, command + "L"))
    if(R not in visited):
      visited.add(R)
      queue.append((R, command + "R"))