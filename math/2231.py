# import sys
# input = sys.stdin.readline

n = int(input())

cnt = 1
digit = len(list(str(n)))
if(digit > 2):
  cnt = n - 10*digit

while True:
  sumOfCnt = sum(list(map(int, list(str(cnt)))))
  if((sumOfCnt + cnt) == n):
    print(cnt)
    break
  elif(cnt >= n): 
    print(0)
    break
  else: cnt += 1

