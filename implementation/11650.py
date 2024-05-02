n = int(input())
sort = sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x : (x[0], x[1]))

for i in sort:
    print(*i)
