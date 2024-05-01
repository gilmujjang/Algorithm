import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
targets = list(map(int, input().split()))

def verticalReverse():
    data.reverse();

def horizontalReverse():
    for i in range(len(data)):
        data[i].reverse()

def rotateClockWise():
    global data
    n = len(data)
    m = len(data[0])
    temp = [[0]*(n) for _ in range(m)]
    for i in range(len(data[0])):
        for j in range(n):
            temp[i][j] = data[n-j-1][i]
    data = temp

def rotateCounterClockWise():
    global data
    n = len(data)
    m = len(data[0])
    temp = [[0]*(n) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = data[j][m-1-i]
    data = temp

def rotateNumberFive():
    global data
    n = len(data)
    m = len(data[0])
    temp = [[0]*(m) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(i < n//2):
                # 1사분면
                if(j < m//2): temp[i][j] = data[i+(n//2)][j]
                # 2사분면
                else : temp[i][j] = data[i][j-(m//2)]
            else:
                # 4사분면
                if(j < m//2): temp[i][j] = data[i][j+(m//2)]
                # 3사분면
                else: temp[i][j] = data[i-(n//2)][j]
    data = temp

def rotateNumberSix():
    global data
    n = len(data)
    m = len(data[0])
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if(i < n//2):
                # 1사분면  
                if(j < m//2): temp[i][j] = data[i][j+(m//2)]
                # 2사분면
                else : temp[i][j] = data[i+(n//2)][j] 
            else:
                # 4사분면
                if(j < m//2): temp[i][j] = data[i-(n//2)][j]
                # 3사분면
                else: temp[i][j] = data[i][j-(m//2)]
    data = temp

for target in targets:
    if target == 1: verticalReverse()
    elif target == 2: horizontalReverse()
    elif target == 3: rotateClockWise()
    elif target == 4: rotateCounterClockWise()
    elif target == 5: rotateNumberFive()
    elif target == 6: rotateNumberSix()


for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j], end=' ')
    print()
