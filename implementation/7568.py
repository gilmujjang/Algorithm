import sys
input = sys.stdin.readline
n = int(input())

# 완전탐색문제
members = []
for _ in range(n):
  weight, height = map(int, input().split())
  members.append([weight, height])

for i in range(n):
  me = members[i]
  cnt = 1
  for j in range(n):
    you = members[j]
    if(you[0] > me[0] and you[1] > me[1]): cnt += 1
  members[i].append(cnt)

for i in range(n):
  print(members[i][2], end=' ')