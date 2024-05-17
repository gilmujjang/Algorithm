
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

AccumulateNumbers = [0]
cnt = 0
for num in input().split():
  cnt += int(num)
  AccumulateNumbers.append(cnt)
  
for _ in range(m):
  i, j = map(int, input().split())
  print(AccumulateNumbers[j] - AccumulateNumbers[i-1])