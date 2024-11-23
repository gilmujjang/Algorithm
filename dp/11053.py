import sys
input = sys.stdin.readline

N = int(input())

numbers = list(map(int, input().split()))
serials = [0 for _ in range(N-1)]
serials.append(1)

for i in range(1, N):
  index = N - i;
  curr = numbers[index-1];
  next = numbers[index];
  for next_index in range(index, N):
    if(curr < numbers[next_index]):
      serials[index-1] = max(serials[next_index], serials[index - 1]);
  serials[index-1] += 1
 

print(max(serials))