import sys
input = sys.stdin.readline

# n = 9
# a = [5,15,100,31,39,0,0,3,26]
# b = [11,12,13,2,3,4,5,9,1]

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
res = 0
for i in range(n):
  res += a[i] * b[i]

print(res)

