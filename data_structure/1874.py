import sys
from collections import deque
input = sys.stdin.readline

num = int(input())
queue = deque()
ans = []

cnt = 1
for _ in range(num):
    target = int(input())
    while target >= cnt:
        queue.append(cnt)
        ans.append('+')
        cnt += 1
    if(queue[-1] == target):
        queue.pop()
        ans.append('-')
    else:
        ans = []
        break
      
if len(ans) == 0: print('NO')
else: print('\n'.join(ans))