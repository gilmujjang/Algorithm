from collections import deque
n, k = map(int, input().split())
s = deque([])
for i in range(1, n + 1):
    s.append(i)
print('<', end='')
while s:
    for i in range(k - 1):
        s.append(s[0])
        s.popleft()
    print(s.popleft(), end='')
    if s:
        print(', ', end='')
print('>')

"""
출처: https://pacific-ocean.tistory.com/233 [코드이터]
너무 안풀려서 베낌
"""
