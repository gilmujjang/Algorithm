# words = ["AAAAAAAAAA", "BBBBBBBBBB"]
# n = len(words)

import sys
input = sys.stdin.readline
n = int(input())
words = []

box = {}

for i in range(n):
    word = input()
    for i in range(len(word)):
        if word[i] in box:
            box[word[i]] += 10**((len(word)) - i - 1)
        else:
            box[word[i]] = 10**(len(word) - i - 1)

sorted_box = sorted(box.values(), reverse=True)
ans = 0
for i in range(len(sorted_box)):
    ans += ((9 - i) * sorted_box[i])

print(ans)