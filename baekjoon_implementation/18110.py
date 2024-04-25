import sys
input = sys.stdin.readline

def roundUp(x):
  if (x - int(x)) >= 0.5: return int(x) + 1
  else: return int(x)

n = int(input())
if n == 0: print(0)
else:
  scores = [ int(input()) for _ in range(n)]
  scores.sort()
  cut = roundUp(n * 0.15)
  trimmed_scores = scores[cut:n-cut]

  print(roundUp(sum(trimmed_scores)/(n-2*cut)))