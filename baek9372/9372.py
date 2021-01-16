# from sys import stdin
# from collections import deque

# # num = 2
# # li = ["3 3","1 2","2 3","1 3","5 4","2 1","2 3","4 3","4 5"]
# num = int(stdin.readline())

# def bfs(x):
#   q = deque()
#   q.append(x)
#   c[x] = 1
#   cnt = 0
#   while q:
#     x = q.popleft()
#     for nx in a[x]:
#       if c[nx] == 0:
#         c[nx] = 1
#         cnt += 1
#         q.append(nx)
#   return cnt

# while num:
#   n, m = map(int,stdin.readline().split())
#   a = [[] for _ in range(n)]
#   c = [0 for _ in range(n)]
#   for _ in range(m):
#     x, y = map(int, stdin.readline().split())
#     a[x-1].append(y-1)
#     a[y-1].append(x-1)

#   ans = 0
#   for i in range(n):
#     if c[i] == 0:
#       ans += bfs(i)
#   print(ans)
#   num -= 1

from sys import stdin
input=stdin.readline
for i in range(int(input())):
  n,m = map(int,input().split())
  for _ in range(m):input()
  print(n-1)