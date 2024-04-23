word = input().lower()
wordSet = list(set(word))
res = []

for i in wordSet:
    res.append(word.count(i))

print("?" if res.count(max(res)) > 1 else wordSet[res.index(max(res))].upper())
