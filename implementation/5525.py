n = int(input())
m = int(input())
IOI = input()


# O(n^2) 이라 50점 맞은 코드
# myIOI = 'I'+n*"OI"
# cnt = 0
# for i in range(m+1 - (2*n + 1)):
#   cut = IOI[i:i + 2*n + 1]
#   if(myIOI == cut): cnt +=1

# print(cnt)

i = 0
temp = 0
cnt = 0

while i < (m-1):
  if IOI[i:i+3] == 'IOI':
    temp += 1
    i += 2
    if temp == n:
      cnt += 1
      temp -= 1
  else:
    i += 1
    temp = 0
print(cnt)