import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    order = input().split()
    command = order[0]
    if(command == 'push'): stack.append(int(order[1]))
    elif(command == 'pop'):print(-1 if len(stack)==0 else stack.pop())
    elif(command == 'size'): print(len(stack))
    elif(command == 'empty'): print(1 if len(stack)==0 else 0)
    elif(command == 'top'): print(-1 if len(stack)==0 else stack[-1])
