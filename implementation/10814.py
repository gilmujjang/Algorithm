
import sys
input = sys.stdin.readline

n = int(input())
members = list(input().split() for _ in range(n))
sorted_members = sorted(members, key=lambda member: int(member[0]))

for member in sorted_members:
    print(member[0], member[1])