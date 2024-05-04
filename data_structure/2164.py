# import sys
# input = sys.stdin.readline

# n = int(input())
# if(n == 1): print(1)
# cards = list(i for i in range(1,n+1))
# for i in range(2, 2*n -1, 2):
#     if(i == 2*(n-1)): print(cards[-1])
#     else:
#         cards.append(cards[i-1])
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
if(n == 1): print(1)
else:
    cards = deque(i for i in range(1,n+1))
    while len(cards)!=1:
        cards.popleft()
        cards.rotate(-1)
    print(cards[0])