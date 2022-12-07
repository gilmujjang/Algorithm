n = 5
l = [4, 3, 5, 7, 9]

# n = int(input())
# l = list(map(int, input().split()))

l.sort()
cnt = 0

while len(l) > 1:
    if l[0] == 0:
        l.pop(0)
    if len(l) == 2:
        cnt += 1
        break
    if len(l) == 1:
        break
    l[0] -= 1
    l.append(l.pop() + l.pop())
    cnt += 1

print(cnt)
