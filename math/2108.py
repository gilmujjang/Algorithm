import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

numbers = []

for _ in range(n):
  numbers.append(int(input()))
numbers.sort()
short_numbers = list(set(numbers))

mode_dictionary = Counter(numbers)

mode_max = max(mode_dictionary.values())

modes = [number for number, count in mode_dictionary.items() if count == mode_max]
modes.sort()
Mode = modes[0] if len(modes) == 1 else modes[1]

Mean = round(sum(numbers)/len(numbers))
Median = numbers[(n//2)]
Spread = abs(numbers[-1] - numbers[0])

print(Mean)
print(Median)
print(Mode)
print(Spread)