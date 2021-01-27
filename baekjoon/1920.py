n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

def binary(s,n,st,en):
  if st>en:
    return 0
  mid = (st+en)//2
  if s[mid]>n:
    return binary(s,n,st,mid-1)
  elif s[mid]<n:
    return binary(s,n,mid+1,en)
  else:
    return 1
a.sort()
for i in b:
  print(binary(a,i,0,n-1))