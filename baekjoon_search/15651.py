n, m = 4, 2

# n, m = map(int,input().split()))

comb = []


def Back_Tracking(depth, n, m):
    print(comb)
    if depth == m:
        print(' '.join(map(str, comb)))
        return

    for i in range(n):
        comb.append(i + 1)
        Back_Tracking(depth + 1, n, m)
        comb.pop()


Back_Tracking(0, n, m)
