import sys

n = int(input())
quest = list(map(int, input().split()))

max_number = max(quest)
result = [True for i in range(max_number-1)]
result.insert(0, False)
result.insert(0, False)


for i in range(2, max_number):
    for j in range(2*i, max_number+1, i):
        result[j] = False
cnt = 0
for num in quest:
    if(result[num] == True): cnt += 1
print(cnt)