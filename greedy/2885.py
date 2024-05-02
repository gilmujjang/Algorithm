import sys
import math
input = sys.stdin.readline

# launch = 6
launch = int(input())

kakao = 2 ** math.ceil(math.log2(launch))
count = 0
print(kakao, end=" ")
while True:
  if launch % kakao == 0:
    print(count)
    break
  else:
    kakao //= 2
    count += 1