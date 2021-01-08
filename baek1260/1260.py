#a,b,n = map(int,stdin.readline().split())

a = 4
b = 5
n = 1

py = ["1 2","1 3","1 4","2 4","3 4"]

    #   1 2 3 4 
    # 1 F T T T
    # 2 F F F T
    # 3 F F F F 
    # 4 F F F F   => 이런식으로 표를 만들고 for문 돌려

node = [[False for col in range(a)] for row in range(a)]

for i in range (b):
    #x,y = map(int,append(stdin.readline().split()))
    x,y = map(int,py[i].split())
    node[x-1][y-1] = True
    node[y-1][x-1] = True

visit_dfs = []
visit_bfs = []

print(node)
def dfs(n):
    visit_dfs.append(n)
    for i in range (a):
        if node[n-1][i] == True:
            if i+1 not in visit_dfs:
                node[n-1][i] = False
                node[i][n-1] = False
                dfs(i+1)   


# def bfs():
#     visit_bfs.append(n)


dfs(n)

print(visit_dfs)