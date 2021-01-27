from sys import stdin
  
a, b = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))

right, left = sum(li)//b, 1

while left <= right:
  num = (right+left)//2
  count = sum([x//num for x in li])
  if count < b:
    right = num - 1
  elif count >= b:
    left = num + 1
    ans = num
print(ans)
