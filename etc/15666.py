import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = sorted(list(set(map(int, input().split()))))
temp = []

def recursion(depth, start):
  if depth == M:
    print(' '.join(map(str, temp)))
    return
  for i in range(numbers.index(start), len(numbers)):
    temp.append(numbers[i])
    recursion(depth+1, numbers[i])
    temp.pop()

recursion(0, numbers[0])