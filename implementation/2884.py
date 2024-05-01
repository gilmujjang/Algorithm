import sys
input = sys.stdin.readline

t, m = map(int, input().split())

print((t - (0 if m>=45 else 1)) if (t - (0 if m>=45 else 1)) >= 0 else (t + 24 - (0 if m>=45 else 1)) , m-45 if m >= 45 else m+60-45)