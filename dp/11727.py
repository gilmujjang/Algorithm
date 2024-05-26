n = int(input())
# 점화식만 구하면 끝
a=b=1
for _ in range(n):
    a,b = b, 2*a+b
print(a%10007)