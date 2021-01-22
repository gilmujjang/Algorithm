# from sys import stdin

li = ["20","7","23","19","10","15","25","8","13"]
arr = []
for i in range(9):
    arr.append(int(li[i]))

arr = sorted(arr)
print(arr)
su = sum(arr)

for i in range(8):
    for j in range(i+1,9):
        if i != j:
            if arr[i]+arr[j]==su-100:
                arr.remove(arr[j])
                arr.remove(arr[i])
                print(arr)                
                exit()
