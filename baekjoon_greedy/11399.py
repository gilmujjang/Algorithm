# n = 5
# ex1 = [3, 1, 4, 3, 2]

n = int(input())
peoples = list(map(int, input().split()))


def atm(peoples):
    peoples.sort()
    acc_time = 0
    sum_time = 0
    for time_cost in peoples:
        acc_time = acc_time + time_cost
        sum_time += acc_time
    print(sum_time)


atm(peoples)

# atm(ex1)