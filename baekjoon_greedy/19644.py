from sys import stdin
from collections import deque

# load = int(stdin.readline())
# ranges, damage = map(int, stdin.readline().split())
# bomb = int(stdin.readline())
# zombie = deque([int(stdin.readline()) for _ in range(load)])

load = 6
ranges = 3
ranges = min(load, ranges)
damage = 2
bomb = 1
zombie = deque([2, 4, 6, 6, 6, 8])

while True:
    if len(zombie) == 0:
        print('YES')
        break
    if (zombie[0] > damage):
        if (bomb):
            zombie[0] = 0
            bomb -= 1
        else:
            print('NO')
            break
    else:
        for i in range(
                0, ranges if ranges < (len(zombie) - 1) else len(zombie) - 1):
            zombie[i] -= damage
    zombie.popleft()
