N, K = 10, 4
num = [4, 1, 7, 7, 2, 5, 2, 8, 4, 1]
k, stack = K, []

# N, K = map(int, input().split())
# num = list(input())
# k, stack = K, []

cnt = 0
for i in range(N):
    while k > cnt and stack and stack[-1] < num[i]:
        stack.pop()
        cnt += 1
    stack.append(num[i])

print(''.join([str(x) for x in stack]))  #터미널에서는 이렇게 해야 출력됨
print(''.join(stack[:N - K]))  #백준에서는 이렇게 해야 통과됨
