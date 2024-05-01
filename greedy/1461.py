import sys
import math
input = sys.stdin.readline

n, k = map(int, input().split());
books = list(map(int, input().split()))
# n, k = 7, 2
# books = [-37, 2, -6, -39, -29, 11, -28]

minus = []
plus = []
distance = []

for book in books:
  if(book > 0): plus.append(book)
  else: minus.append(-book)


minus.sort(reverse=True)
plus.sort(reverse=True)

for i in range (math.ceil(len(minus) / k)):
  distance.append(minus[k * i])

for i in range (math.ceil(len(plus) / k)):
  distance.append(plus[k * i])

distance.sort(reverse=True)

res = distance[0]
for d in range(len(distance)-1):
  res += 2* distance[d + 1]


print(res)
