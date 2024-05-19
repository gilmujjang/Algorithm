N, r, c = map(int, input().split())

def recursion(N, r, c):
  if(N == 0): return 0
  else:
    return 2*(r%2) + c%2 + 4*recursion(N-1, r//2, c//2)
  
print(recursion(N, r, c))