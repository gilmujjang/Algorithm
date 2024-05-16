import sys
input = sys.stdin.readline

domain_num, quest_num = map(int, input().split())

storage = dict()

for n in range(1, domain_num+1):
  domain, password = map(str, input().split())
  storage[domain] = password

for n in range(quest_num):
  domain = input().rstrip()
  print(storage[domain])
