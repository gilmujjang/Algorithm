n = int(input())

cnt = 1
title = 666

while True:
    isDevil = str(title).find('666') != -1
    if(n <= cnt and isDevil):
        print(title)
        break
    if(isDevil):
       cnt += 1
    title += 1