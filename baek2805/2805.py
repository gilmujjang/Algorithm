import sys

def input():
  return sys.stdin.readline().rstrip()
  
a,b = map(int, input().split())
li = list(map(int, input().split()))

left, right, ans = 0,max(li),0

while left<=right:
  middle = (left+right)//2
  tree = 0
  for i in range(a):
    if middle<li[i]:
      tree += li[i] - middle
  if tree >= b:
    ans = middle
    left = middle+1
  elif tree<b:
    right = middle-1
print(ans)