import sys

input = sys.stdin.readline

# n = 10
# plus = [1,2,3,4,5,6]
# minus = [-5,-4,-3,-1,0]

n = int(input())
plus = []
minus = []
for i in range(n):
  temp = int(input())
  if(temp > 0): plus.append(temp)
  else: minus.append(temp)

plus.sort(reverse=True)
minus.sort()

sum = 0

for i in range(len(plus)//2):
  sum += max(plus[2*i]*plus[2*i+1], plus[2*i] + plus[2*i+1])
if(len(plus)%2 != 0): sum += plus[-1]

for i in range(len(minus)//2):
  sum += max(minus[2*i]*minus[2*i+1], minus[2*i] + minus[2*i+1])
if(len(minus)%2 != 0): sum += minus[-1]

print(sum)