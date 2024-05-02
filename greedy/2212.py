import sys
input = sys.stdin.readline

# n = 6
# k = 2
# sensors = [1, 6, 9, 3, 6, 7]

n = int(input())
k = int(input())
sensors = list(map(int, input().split()))

sensors.sort(reverse=True)
distance = []

for i in range (0, n-1):
  distance.append(sensors[i] - sensors[i+1])
distance.sort()

print(sum(distance[:n-k]))
