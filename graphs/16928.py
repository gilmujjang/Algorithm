import sys
from collections import deque 

# 처음에는 모든 칸 마다 소요되는 횟수를 저장해가며 풀려면 dp인것 같았지만
# 태그가 bfs인게 이상해서 해설을 찾아보니까 탐색으로 구현되어있었다
# bfs에서 큐에 담는 행위가 dp에서 메모 하는것과 같은 기능을 하고있다.

input = sys.stdin.readline

N, M = map(int, input().split())

ShortCut = dict()

distantBoard = [0]*101

for _ in range(N + M):
    entrance, egress = map(int, input().split())
    ShortCut[entrance] = egress

queue = deque([1])

while queue:
    position = queue.popleft()
    if(position == 100):
        print(distantBoard[100])
        break
    for dice in range(1, 7):
        nextPosition = position + dice
        if(nextPosition <= 100 and distantBoard[nextPosition] == 0):
            if(nextPosition in ShortCut.keys()): nextPosition = ShortCut[nextPosition]
            if(distantBoard[nextPosition] == 0):distantBoard[nextPosition] = distantBoard[position] + 1
            queue.append(nextPosition)
