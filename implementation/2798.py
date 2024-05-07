import sys

n, m = map(int, input().split())

cards = sorted(list(map(int, input().split())))

result = []
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            cnt = cards[i] + cards[j] + cards[k]
            if(cnt == m):
               result.append(cnt)
               break
            elif(cnt < m): result.append(cnt)
            else: 
                break
print(max(result))
