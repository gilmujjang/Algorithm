from sys import stdin

num = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
budget = int(stdin.readline())

li.sort()

minimum = 1
limit = max(li)

while minimum<=limit:
  mid = (limit+minimum)//2
  budgetsum = sum([mid if x > mid else x for x in li])

  if budget>= budgetsum:
    minimum = mid +1
    ans = mid
  else:
    limit = mid - 1

print(ans)