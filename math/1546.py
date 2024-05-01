import sys
input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))

best = max(scores)
new_scores = []

for score in scores:
  new_scores.append((score/best)*100)

print(sum(new_scores)/(len(new_scores)))