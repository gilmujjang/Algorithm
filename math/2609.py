import sys
input = sys.stdin.readline

x, y = map(int, input().split())

# Greatest common divisor
def gcd(x, y):
  if(y == 0): return x
  else: return gcd(y, x%y)

# Least common multiple
def lcm(x, y):
  return (x*y)//gcd(x,y)

print(gcd(x, y))
print(lcm(x,y))