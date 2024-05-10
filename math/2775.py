import sys
input = sys.stdin.readline

r = int(input())

storage = [list(0 for _ in range(15))for _ in range(15)]

def recursion(k, n):
  if(storage[k][n] != 0): return storage[k][n]
  elif(k == 0):
    storage[k][n] = n
    return n
  elif(n==1):
    storage[k][n] = 1
    return 1
  else: 
    ans = recursion(k-1, n) + recursion(k, n-1)
    storage[k][n] = ans
    return ans

for _ in range(r):
  k = int(input())
  n = int(input())
  print(recursion(k, n))

