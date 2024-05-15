import sys
input = sys.stdin.readline
n = int(input())
storage = set()
for _ in range(n):
    command_input = input().rstrip()
    if(command_input == 'all'): 
        storage = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif(command_input == 'empty'): storage = set()
    else:
        command, num = command_input.split()
        num = int(num)
        int(num)
        if(command == 'add'): storage.update([num])
        elif(command == 'remove'):
            if(num in storage): storage.remove(num)
        elif(command == 'check'): print(1 if(num in storage) else 0)
        elif(command == 'toggle'): storage.remove(num) if(num in storage) else storage.update([num])