import sys
from collections import deque
n = int(input())

def func(query, array):
  deq = deque(array)
  flag = True
  for command in query:
    if(command == 'R'): flag = not flag
    if(command == 'D'):
      if(len(deq) == 0): return 'error'
      if(flag == True): deq.popleft()
      else: deq.pop()
  if(flag == False): deq.reverse()
  return "[" + ','.join(str(i) for i in list(deq))+"]"

for i in range(n):
  query = sys.stdin.readline().rstrip()
  num = int(input())
  array_str = sys.stdin.readline().rstrip()
  array = [] if num == 0 else array_str[1:-1].split(',')
  print(func(query, array))
