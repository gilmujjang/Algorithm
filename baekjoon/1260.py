# from sys import stdin
# a,b,n = map(int,stdin.readline().split())

a = 5
b = 5
n = 3

py = ["5 4","5 2","1 2","3 4","3 1"]

    #   1 2 3 4 
    # 1 F T T T
    # 2 F F F T
    # 3 F F F F 
    # 4 F F F F 


    #   1 2 3 4 5
    # 1 F T T F F
    # 2 T F F F T
    # 3 T F F T F
    # 4 F F T F T
    # 5 F T F F T

node = [[False for col in range(a)] for row in range(a)]
node1 = [[False for col in range(a)] for row in range(a)]
for i in range (b):
    #x,y = map(int,stdin.readline().split())
    x,y = map(int,py[i].split())
    node[x-1][y-1] = True
    node[y-1][x-1] = True
    node1[x-1][y-1] = True
    node1[y-1][x-1] = True

visit_dfs = []
visit_bfs = []


def dfs(n):
    visit_dfs.append(n)
    for i in range (a):
        if node[n-1][i] == True:
            if i+1 not in visit_dfs:
                node[n-1][i] = False
                node[i][n-1] = False
                dfs(i+1)   

def bfs(n):
    golist = [n]
    while golist:
        start = golist.pop(0)
        visit_bfs.append(start)
        for i in range (a):
            if node1[start-1][i] == True:
                if i+1 not in visit_bfs:
                    if i+1 not in golist:
                        node1[start-1][i] = False
                        node1[i][start-1] = False
                        golist.append(i+1)
                    

dfs(n)
bfs(n)
print(" ".join(map(str,visit_dfs)))
print(" ".join(map(str,visit_bfs)))
