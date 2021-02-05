from sys import stdin

# n,m = 3,5
# li = ["42101","22100","22101"]
# for i in range(n):
#   arr.append(list(map(int,li[i])))

n,m = map(int,stdin.readline().split())
a = min(n,m)
b = 0
arr = []

for i in range(n):
  arr.append(list(int, stdin.readline()))

for i in range(n):
  for j in range(m):
    for q in range(a):
      if i+q<n and j+q<m:
        if arr[i][j] == arr[i][j] and arr[i][j] == arr[i+q][j] and arr[i][j] == arr[i+q][j+q]:
          if b < q:
            b = q

print((b+1)(b+1))
#왜인지 모르겠는데 stdin.readline() 하면 런타임에러(ValueError)가 난다