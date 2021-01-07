from sys import stdin

num = int(stdin.readline())

li = list(map(int, stdin.readline().split()))

li.sort()

left = 0
right = num-1

while left<=right:
  mid = (right - left)//2
  ans =0
  
print(ans)