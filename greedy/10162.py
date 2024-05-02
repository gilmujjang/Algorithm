# example1 = 100
# example2 = 189

food = int(input())

def microwave(food):
  if food%10 == 0:
    a = food//300
    food = food%300
    b = food//60
    food = food%60
    c = food//10
    print(a, b, c)
  else:
    print(-1)

microwave(food)

# microwave(example1)
# microwave(example2)