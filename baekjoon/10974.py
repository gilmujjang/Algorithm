from itertools import permutations

n = int(input())
li = [i for i in range(1,n+1)]

for a in list(permutations(li)):
  for i in a:
    print(i, end=' ')
  print()