import sys
input = sys.stdin.readline

# string = '55-50+40'
string = str(input())

split = string.split('-')
cnt = 0 if split[0] == '' else sum(list(map(int, split[0].split('+'))))
for i in range(len(split)-1):
  temp = sum(list(map(int, split[i+1].split('+'))))
  cnt -= temp
print(cnt)