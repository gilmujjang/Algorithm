N = int(input())

stair = [0]

for _ in range(N):
  stair.append(int(input()))

if(N == 1): print(stair[1])
elif(N==2): print(stair[1]+stair[2])
else:
    storage = [0, stair[1], stair[1]+stair[2]]
    for i in range(3, N+1):
        storage.append(max(storage[i-2] + stair[i], storage[i-3]+stair[i-1]+stair[i]))
    print(storage[-1])