# test_case = 1
# num = 5
# newbie_results = [[3, 2], [1, 4], [4, 1], [2, 3], [5, 5]]
import sys


def employ(num, newbie_results):
    newbie_results.sort()
    sucess = 1
    best_interview = newbie_results[0][1]
    for i in range(1, num):
        if best_interview > newbie_results[i][1]:
            sucess += 1
            best_interview = newbie_results[i][1]

    print(sucess)


test_case = int(sys.stdin.readline())
for i in range(0, test_case):
    num = int(sys.stdin.readline())
    newbie_results = []
    for i in range(num):
        paper, interview = map(int, sys.stdin.readline().split())
        newbie_results.append([paper, interview])
    employ(num, newbie_results)

# employ(num, newbie_results)
