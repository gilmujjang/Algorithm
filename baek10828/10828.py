input = [
  '14',
  'push', '1',
  'push', '2',
  'top',
  'size',
  'empty',
  'pop',
  'pop',
  'pop',
  'size',
  'empty',
  'pop',
  'push', '3',
  'empty',
  'top'
]
num = []
s = 0
q = 0

for i in range(1,len(input)):
  now = input[i]
  if input[i]=='push':
    num.append(input[i+1])
    s = s + 1
  
  if now=='pop':
    if s>0:
      print(num[s-1])
      del num[s-1]
      s = s - 1;
    else:
      print(-1)
    
  if now=='size':
    print(s)
  
  if now=='empty':
    if s>0:
      print(0)
    else:
      print(1)
  
  if now=='top':
    if s>0:
      print(num[s-1])
    else:
      print(-1)