import sys
input = sys.stdin.readline

# n, k = 4, 2
# cards = [4, 2, 3, 1]

n, k = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()

for i in range (k):
  temp = cards[0] + cards[1]
  cards[0] = temp
  cards[1] = temp
  cards.sort()

print(sum(cards))