import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(N)]

height_list = sorted(sum(blocks, []), reverse=True)
MIN_HEIGHT = min(height_list)
MAX_HEIGHT = max(height_list)

result = []

for target_height in range(MIN_HEIGHT-1, MAX_HEIGHT+1):
    time = 0
    block_cnt = B
    flag = True
    for block_height in height_list:
        block_diff = target_height - block_height
        if(block_cnt < block_diff > 0):
            flag = False
            break
        if(block_diff < 0):
            block_cnt -= block_diff
            time -= 2*block_diff
        else:
            block_cnt -= block_diff
            time += block_diff
    if(flag): result.append([time, target_height])

result.sort(key=lambda x: (x[0], -x[1]))
print(result[0][0], result[0][1])