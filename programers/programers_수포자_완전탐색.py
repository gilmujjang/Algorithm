def solution(answers):
    man1 = 0
    man2 = 0
    man3 = 0
    num = len(answers)

    def pickmaker(pattern):
        pick = []
        while len(pick) < num:
            pick = pick + pattern
        while len(pick) > num:
            pick.pop()
        return pick

    man1_pick = pickmaker([1, 2, 3, 4, 5])
    man2_pick = pickmaker([2, 1, 2, 3, 2, 4, 2, 5])
    man3_pick = pickmaker([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])

    for i in range(num):
        if man1_pick[i] == answers[i]:
            man1 += 1
        if man2_pick[i] == answers[i]:
            man2 += 1
        if man3_pick[i] == answers[i]:
            man3 += 1
    li = [man1, man2, man3]
    m = max(li)
    answer = []
    for i in range(len(li)):
        if li[i] == m:
            answer.append(i + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
