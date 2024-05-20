import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def recursion(x, y, r):
    global white, blue
    temp = paper[x][y]
    for i in range(x, x+r):
      for j in range(y, y+r):
        if(temp != paper[i][j]):
          new_r = r//2
          recursion(x, y, new_r)
          recursion(x+new_r, y, new_r)
          recursion(x+new_r, y+new_r, new_r)
          recursion(x, y+new_r, new_r)
          return 
    if(temp == 0): white += 1
    else: blue +=1

recursion(0, 0, N)

print(white)
print(blue)
  