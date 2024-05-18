n = int(input())

storage = [0,1,2,3,5,8]

for i in range(5, n):
    storage.append((storage[-1] + storage[-2])%10007)
print(storage[n])

# 배열 없이 하는법 
# a=b=1
# for _ in range(n):
#     a,b = b, a+b
# print(a%10007)