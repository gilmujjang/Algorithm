import sys
from collections import deque
# deque를 사용하지 않는경우가 더 빠름
input = sys.stdin.readline

n = int(input())

deq = deque()
for _ in range(n):
    order = input().split()
    command = order[0]
    if(command == 'push_front'): deq.appendleft(int(order[1]))
    elif(command == 'push_back'): deq.append(int(order[1]))
    elif(command == 'pop_front'): print(-1 if len(deq)==0 else deq.popleft())
    elif(command == 'pop_back'): print(-1 if len(deq)==0 else deq.pop())
    elif(command == 'size'): print(len(deq))
    elif(command == 'empty'): print(1 if len(deq)==0 else 0)
    elif(command == 'front'): print(-1 if len(deq)==0 else deq[0])
    elif(command == 'back'): print(-1 if len(deq)==0 else deq[-1])
# deque = []
# for _ in range(n):
#     order = input().split()
#     command = order[0]
#     if(command == 'push_front'): deque.insert(0, int(order[1]))
#     elif(command == 'push_back'): deque.append(int(order[1]))
#     elif(command == 'pop_front'): print(-1 if len(deque)==0 else deque.pop(0))
#     elif(command == 'pop_back'): print(-1 if len(deque)==0 else deque.pop())
#     elif(command == 'size'): print(len(deque))
#     elif(command == 'empty'): print(1 if len(deque)==0 else 0)
#     elif(command == 'front'): print(-1 if len(deque)==0 else deque[0])
#     elif(command == 'back'): print(-1 if len(deque)==0 else deque[-1])

