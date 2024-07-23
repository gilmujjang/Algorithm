import sys
input = sys.stdin.readline

n = int(input())
fruits = list(map(int, input().split()))

start_pointer, end_pointer = 0, 1
kind = [fruits[0]]
answer = 0
next_start_pointer = 0
while end_pointer < n:
    if len(kind) == 1:
        if fruits[end_pointer] not in kind:
            kind.append(fruits[end_pointer])

    else:
        if fruits[end_pointer] not in kind:
            answer = max(answer, end_pointer - start_pointer)
            # 딸기와 사과가 있었으면 앞에 딸기만 제거
            for i in range(len(kind)):
                if kind[i] != fruits[next_start_pointer]:
                    kind.pop(i)
                    break

            kind.append(fruits[end_pointer])
            start_pointer = next_start_pointer

    if fruits[end_pointer - 1] != fruits[end_pointer]:
        next_start_pointer = end_pointer
    end_pointer += 1

answer = max(answer, n-start_pointer)
print(answer)