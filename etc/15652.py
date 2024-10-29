import sys
input = sys.stdin.readline

N, M = map(int, input().split())

temp = []

def recursion2(start):
  if len(temp) == M:
    print(' '.join(map(str, temp)))
    return

  for i in range(start, N+1):
    temp.append(i)
    recursion2(i)
    temp.pop();

recursion2(1)
