# from sys import stdin

li = ["20","7","23","19","10","15","25","8","13"]
arr = []
for i in range(9):
    arr.append(int(li[i]))

arr = sorted(arr)
print(arr)
su = sum(arr)
a = 0
b = 0

for i in range(8):
    for j in range(i+1,9):
        if i != j:
            if arr[i]+arr[j]==su-100:
                a = arr[i]
                b = arr[j]

arr.remove(a)
arr.remove(b)

for i in arr:
    print(i)