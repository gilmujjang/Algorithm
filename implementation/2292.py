n = int(input())

if(n == 1): print(1)
else:
    result = ((4*(n-1)-1)/12)**0.5 + 0.5
    print(int(result)+1)