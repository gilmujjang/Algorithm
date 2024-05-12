
import sys
input = sys.stdin.readline
n = int(input())
MAX = 10001
result = [0 for _ in range(MAX)]
for _ in range(n):
    num = int(input())
    result[num] += 1

for i in range(MAX):
    value = result[i]
    if(value != 0):
        for _ in range(value):
            print(i)
