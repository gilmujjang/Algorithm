import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
temp = []

def recursion(depth):
  if depth == M:
    print(' '.join(map(str, temp)))
    return
  for i in range(N):
    if numbers[i] not in temp:
      temp.append(numbers[i])
      recursion(depth+1)
      temp.pop()

recursion(0)