import sys
# input = sys.stdin.readline

x, y = map(int, input().split())

chess_board = list(str(input()) for _ in range(x))

result = []

for i in range(x-7):
  for j in range(y-7):
    black_cnt = 0
    white_cnt = 0
    # 흰색으로 시작하는 경우
    for a in range(i, i+8):
      for b in range(j, j+8):
        if((a+b)%2 == 0):
          if(chess_board[a][b] != 'W'): white_cnt+=1 
          if(chess_board[a][b] != 'B'): black_cnt+=1 
        else:
          if(chess_board[a][b] != 'B'):white_cnt+=1 
          if(chess_board[a][b] != 'W'):black_cnt+=1 

    result.append(black_cnt)
    result.append(white_cnt)

print(min(result))