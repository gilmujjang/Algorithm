import sys
input = sys.stdin.readline
start, end = map(int, input().split())

result = [True for _ in range(end+1)]
result[0] = False
result[1] = False

for i in range(2, end):
    for j in range(2*i, end+1, i):
        result[j] = False

for i in range(start, end+1):
    if(result[i] == True): print(i)
