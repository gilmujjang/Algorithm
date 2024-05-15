n = int(input())

numbers = list(int(input()) for _ in range(n))

MAX = max(numbers)

storage = [[0, 0] for _ in range(MAX+2)]
storage[0] = [1, 0]
storage[1] = [0, 1]

for i in range(2, MAX+2):
    storage[i] = [storage[i-1][0] + storage[i-2][0], storage[i-1][1] + storage[i-2][1]]

for num in numbers:
    print(storage[num][0], storage[num][1])