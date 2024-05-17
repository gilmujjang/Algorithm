n = int(input())

storage = [0,1,2,4,7]
for i in range(7):
    storage.append(storage[-1] + storage[-2] + storage[-3])

for _ in range(n):
    i = int(input())
    print(storage[i])
