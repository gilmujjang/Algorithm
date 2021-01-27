import sys
def input():
  return sys.stdin.readline().rstrip()
  

n, m = map(int,input())

a = set()
b = set()

for i in range(n):
  a.add(input())

for i in range(m):
  b.add(input())

d = list(a & b)
print(len(d))

for i in sorted(d):
  print(i)