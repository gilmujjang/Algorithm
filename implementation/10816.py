import sys
input = sys.stdin.readline

a = int(input())
targets = list(map(int, input().split()))
b = int(input())
quest = list(map(int, input().split()))

dict = {}
for target in targets:
  if(target in dict): dict[target] += 1
  else: dict[target] = 1

for q in quest:
  print(dict.get(q, 0), end=' ')