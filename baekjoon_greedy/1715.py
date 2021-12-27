# cards = [30, 40, 50, 60]
# n = len(cards)

import heapq
import sys
input = sys.stdin.readline
n = int(input())
cards = list(int(input()) for _ in range(n))


def card_shuffle(cards):
    cards.sort()
    cnt = 0
    for _ in range(n - 1):
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        print(a + b)
        cnt += a + b
        heapq.heappush(cards, a + b)

    print(cnt)


card_shuffle(cards)
