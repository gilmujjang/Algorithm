import sys
input = sys.stdin.readline

# price = 1000 - 380

price = 1000 - int(input())

coins = [500, 100, 50, 10, 5, 1]

cnt = 0

for coin in coins:
    if price // coin > 0:
        cnt += price // coin
        price = price % coin

print(cnt)