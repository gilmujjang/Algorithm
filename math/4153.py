import sys

input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    if(a == 0): break
    array = [a, b, c]
    array.sort()
    if(array[0]**2 + array[1]**2 == array[2]**2): print('right')
    else: print('wrong')
