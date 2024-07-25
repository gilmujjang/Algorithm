import math
n = int(input())

def kaing(M, N, x, y):
  lcm = math.lcm(M, N)
  year = x
  while year <= lcm:
    if ((year-1) % N) == y-1: return year
    year += M
  return -1

for i in range(n):
  M, N, x, y = map(int, input().split())
  print(kaing(M, N, x, y))
