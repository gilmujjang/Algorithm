import sys

n = int(input())
guitar = []
for _ in range(n):
  serial = input()
  sum_number = 0
  for i in serial:
    if i.isdigit():
      sum_number += int(i)
  guitar.append((serial, sum_number))
 
result = sorted(
  guitar, key=lambda x : (len(x[0]), x[1], x[0])
)

for s in result:
  print(s[0])

