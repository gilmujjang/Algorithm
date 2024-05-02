data = input()
# data = '0001100'

cnt = [0, 0]

temp = '2'
for c in data:
  if(c != temp): 
    temp = c
    cnt[int(c)] = cnt[int(c)] + 1

print(min(cnt))
