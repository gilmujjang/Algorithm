# n = 4
# m = 42

n, m = map(int, input().split())

odd_num = ["3", "5", "7", "9"]
str_m = str(m)
cnt = 1

while True:
    last_num = str_m[-1:]
    if (n == m):
        print(cnt)
        break

    if (n > m):
        print(-1)
        break

    if (last_num in odd_num):
        print(-1)
        break

    if (last_num == "1"):
        str_m = str_m[:-1]
        cnt += 1
    else:
        str_m = str(int(m / 2))
        cnt += 1
    m = int(str_m)
