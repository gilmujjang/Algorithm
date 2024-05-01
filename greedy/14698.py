import sys
import heapq
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    slime = [*map(int, input().split())]  # *map은 새 리스트를 반환한다
    heapq.heapify(slime)
    result = 1
    p = 1000000007
    while (len(slime) > 1):
        slime1 = heapq.heappop(slime)
        slime2 = heapq.heappop(slime)
        newSlime = slime1 * slime2
        result *= newSlime
        heapq.heappush(slime, newSlime)

    print(result % p)