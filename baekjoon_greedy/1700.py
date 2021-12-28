n, m = 2, 7
elec = [2, 3, 2, 3, 1, 2, 7]

# n, m = map(int, input().split())
# elec = list(map(int, input().split()))

plug = []
cnt = 0
print("FUCkCDkjCkljoCSDk;ljfk;ljfsdk;ljfasdk;lj")
while len(elec) != 0:
    print('-----------------')
    print('my plug ', plug)
    if n >= m:  #플러그가 가전제품보다 많으면
        break

    code = elec[0]
    print(code)
    print('this code is', code)

    if code in plug:  #이미 꼽혀 있으면
        print(code, 'already pluged in')
        elec.pop(0)
        pass

    else:  #안꼽혀 있으면

        if len(plug) < n:  #빈 콘센트가 있으면
            print('empty code exist,', code, 'in')
            plug.append(code)  #코드 꼽는다
            elec.pop(0)

        else:  #빈 콘센트가 없으면
            print('calculate')
            plug_count = plug[:]

            for item in elec:
                print('plug_count', plug_count)

                if item in plug_count:  #뺄 후보에서 곧 쓸거는 제외
                    plug_count.remove(item)
                    print('remove candidate', plug_count)

                if len(plug_count) == 1:  #이미 꼽혀있는것중에 가장 늦게 사용하는게 나오면
                    print(plug_count[0], 'remove')
                    plug.remove(plug_count[0])
                    cnt += 1
                    plug.append(code)
                    elec.pop(0)
                    print(code, 'in')
                    break

            if len(plug_count) > 1:  #안쓰는게 여러개이면 아무거나 뽑음
                print(plug_count[-1], 'removed,', code, 'in')
                plug.remove(plug_count[-1])
                cnt += 1
                plug.append(code)
                elec.pop(0)
                print(code, 'in')
            else:
                print('trap')
    print('next elec is', elec)

print(cnt)
