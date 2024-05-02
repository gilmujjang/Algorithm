n = 7
weights = [3, 1, 6, 2, 7, 30, 1]

n = int(input())
weights = list(map(int, input().split()))

weights.sort()
cnt = 1
for weight in weights:
    if cnt < weight:
        break
    else:
        cnt += weight

print(cnt)
