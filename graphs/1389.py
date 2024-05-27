import sys

input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
friend_map = list(list(INF for _ in range(N+1)) for _ in range(N+1))

for i in range(1, N+1):
  friend_map[i][i] = 0

for _ in range(M):
  start, end = map(int, input().split())
  friend_map[start][end] = 1
  friend_map[end][start] = 1

for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
          friend_map[a][b] = min(friend_map[a][b], friend_map[a][k] + friend_map[k][b])


bacon_nums = []
for row in friend_map[1:N+1]:
   bacon_nums.append(sum(row[1:N+1]))
min_bacon_num = min(bacon_nums)

for i in range(N):
   if(bacon_nums[i] == min_bacon_num):
      print(i+1)
      break