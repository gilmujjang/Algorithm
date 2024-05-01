import sys

input = sys.stdin.readline

# n = 11
# meetings = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]

n = int(input())
meetings = []
for i in range(n):
  meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x:(x[1], x[0]))
cnt = 0
endTime = 0

for meeting in meetings:
  if(meeting[0] >= endTime):
    endTime = meeting[1]
    cnt += 1

print(cnt)