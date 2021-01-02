import sys
def input():
  return sys.stdin.readline()

n = int(input())
li = []
for _ in range(n):
  word = input()
  li.append(word)
 
result = sorted(
  li, key=lambda x : (len(x), x)
)
result = list(set(result)) 

for s in result:
  print(s)

