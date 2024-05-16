n = int(input())

storage = [1,1,1,2,2]
for i in range(95):
    storage.append(storage[-3] + storage[-4] + storage[-5])

for _ in range(n):
    i = int(input())
    print(storage[i-1])