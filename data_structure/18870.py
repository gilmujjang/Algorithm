import sys
input = sys.stdin.readline
n = int(input())

coordinates = list(int(num) for num in input().split())
sortedArray = sorted(list(set(coordinates)))

coordinateDict = {}

for c in range(len(sortedArray)):
  coordinateDict[sortedArray[c]] = c

for c in coordinates:
  print(coordinateDict[c], end=' ')