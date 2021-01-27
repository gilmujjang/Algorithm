from sys import stdin

a,b = map(int, stdin.readline().split())
li = list(map(int, stdin.readline().rstrip().split()))

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