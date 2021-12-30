def solution(people, limit):
    answer = 0
    people.sort()
    while people:
        boat = people.pop()
        answer += 1
        man_in_boat = 1
        for man in people:
            if man_in_boat != 2 and boat + man <= limit:
                boat += man
                man_in_boat += 1
                people.remove(man)
    return answer


print(solution([70, 50, 80, 50, 10, 10, 10, 10], 100))
