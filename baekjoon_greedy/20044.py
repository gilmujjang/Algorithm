import sys
input = sys.stdin.readline

n = int(input())
level = list(map(int, input().split()))

# n = 3
# level = [1, 7, 3, 5, 9, 2]

level.sort()

teams = []

for i in range (0, n):
    teams.append(level[i] + level[2*n-i-1])

teams.sort()
print(teams[0])