import sys
input = sys.stdin.readline

n, k = map(int, input().split())

def factorial(x):
  return x * factorial(x-1) if x > 1 else 1

numerator = factorial(n)
denominator  = factorial(k) * factorial(n-k)

print(int(numerator/denominator))