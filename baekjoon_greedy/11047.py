import sys
input = sys.stdin.readline

# n = 10 
# target = 4790
# coins = [1,
# 5,
# 10,
# 50,
# 100,
# 500,
# 1000,
# 5000,
# 10000,
# 50000]

n, target = map(int, input().split()) 
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0

for coin in coins:
  c = target//coin
  if(c >= 1):
    target -= c * coin
    cnt += c
  if(target == 0): break

print(cnt)

