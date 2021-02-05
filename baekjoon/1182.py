from sys import stdin

def recursive(id, sum):
  global cnt
  if id >= n:
    return
    
  # sum += s_li[id]
  # if sum == s:
  #   cnt += 1
  # recursive(id + 1, sum-s_li[id])
  # recursive(id + 1, sum)

# n,s = 5,0
# s_li = [-7, -3, -2, 5, 8]
n,s = map(int, stdin.readline().split())
s_li = list(map(int, stdin.readline().split()))
cnt = 0
recursive(0,0)
print(cnt)