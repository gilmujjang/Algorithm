import sys
input = sys.stdin.readline

num, quest = map(int, input().split())

storage_text = dict()
storage_num = []

for n in range(1, num+1):
  Pokemon = input().rstrip()
  storage_text[Pokemon] = n
  storage_num.append(Pokemon)

for n in range(quest):
  q = input().rstrip()
  try:
    intQ = int(q)
    print(storage_num[intQ-1])
  except ValueError:
    print(storage_text[q])
