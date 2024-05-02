import sys
input = sys.stdin.readline

# n = 5
# ropes = [1,2,3,4,5]

n = int(input())
ropes = []
for i in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)
res = []

for i in range(n):
  res.append((i+1)*ropes[i])

print(max(res))