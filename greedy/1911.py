n = 4
l = 3
puddle = [[1, 6], [13, 17], [8, 12]]

# n, l = map(int, input().split())
# puddle = [list(map(int, input().split())) for _ in range(n)]

puddle.sort()
cnt = 0
coverage = 0
for start, end in puddle:
    if coverage < start:
        coverage = start
    size = end - coverage

    if (size % l == 0):
        board = size // l
    else:
        board = (size // l) + 1
    cnt += board
    coverage = coverage + (l * board)

print(cnt)
