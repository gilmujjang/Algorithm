
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())

target = a*b*c

for i in range(10):
    print(str(target).count(str(i)))