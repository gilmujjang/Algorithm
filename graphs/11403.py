import sys

input = sys.stdin.readline

N = int(input())

node = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
  for j in range(N):
    for k in range(N):
      if(node[j][k] == 0 and node[j][i] == 1 and node[i][k] == 1): node[j][k] = 1

# 정석은 점화식에 따라 플로이드 워셜 알고리즘을 수행함
# 해당 문제에서는 0과 1로만 구분하지만 정석은 거리를 계산함
# for k in range(N):
#     for a in range(N):
#         for b in range(N):
#             node[a][b] = min(node[a][b], node[a][k] + node[k][b])

for row in node:
  for num in row:
    print(num, end=' ')
  print()