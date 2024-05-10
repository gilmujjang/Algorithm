import math

A, B, V = map(int, input().split())

distance = V - A
distancePerDay = A - B
print(1 + math.ceil(distance/distancePerDay))