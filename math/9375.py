import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
  m = int(input())
  inventory = dict()
  for _ in range(m):
    _, item = input().split()
    if item in inventory: inventory[item] = inventory[item]+1
    else: inventory[item] = 1
  cnt = 1
  for i in inventory.values():
    cnt *= (i+1)
  print(cnt-1)
