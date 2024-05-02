n = 10000
# n = int(input())

dp = {1: 0, 2: 1, 3: 1, 4: 2, 6: 2, 9: 2}


def solution(n):
    if n in dp: return dp[n]
    m = 1 + min(solution(n // 2) + n % 2, solution(n // 3) + n % 3)
    dp[n] = m
    return m


print(solution(n))
print(dp)