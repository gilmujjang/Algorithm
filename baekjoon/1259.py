n = ['121', '1231', '12421', '0']

while True:
    n = input()
    if (n == '0'):
        break
    for i in range(len(n)):
        if (i == len(n) - 1):
            print('yes')
            break
        if (n[i] != n[len(n) - 1 - i]):
            print('no')
            break
