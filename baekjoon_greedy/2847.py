import sys
input = sys.stdin.readline

# n = 4
# scores = [5,3,7,5]

n = int(input())
scores = []
for i in range(n):
    scores.append(int(input()))

cnt = 0

for i in range(n-1):
  if scores[n-1-i] <= scores[n-2-i]:
    cnt += (scores[n-2-i] - scores[n-1-i]) + 1
    scores[n-2-i] = scores[n-1-i]-1

print(cnt)