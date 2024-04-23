n = int(input())

for _ in range(n):
    x, y, z = map(int, input().split())
    floor = (z % x)
    number = (z // x) + 1
    if floor == 0: 
        floor = x
        number -= 1
    print(str(floor) + ('0'+str(number) if number < 10 else str(number)))
