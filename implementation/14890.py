import sys
input = sys.stdin.readline

n, l = map(int, input().split())

contour = list( list(map(int, input().split())) for _ in range(n))

cnt = 0

def go(road):
  used = [False for _ in range(n)]
  for i in range(n-1):
    height = road[i] - road[i+1]
    if(abs(height) > 1): return False
    else:
      if(height == 1):
        for j in range(l):
          if(i+j+1 > n-1): return False
          if(road[i+1] != road[i+1+j]): return False
          if(used[i+1+j]==True): return False
          else: used[i+1+j] = True
      elif(height == -1):
        for j in range(l):
          if(i-j < 0): return False
          if(road[i] != road[i-j]): return False
          if(used[i-j]==True): return False
          else: used[i-j] = True
  return True



for i in range(n):
  if(go(contour[i])): cnt+=1

for j in range(n):
  if(go([contour[i][j] for i in range(n)])): cnt+=1

print(cnt)
