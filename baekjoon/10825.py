import sys
def input():
  return sys.stdin.readline().rstrip()
  
scores = []
for _ in range(int(input())):
  name, kor, eng, math = input().split()
  kor, eng, math = map(int, [kor, eng, math])
  scores.append((kor, eng, math, name))
 
result = sorted(
  scores, key=lambda score: (-score[0], score[1], -score[2], score[3])
) 

for name in result:
  print(name[3])