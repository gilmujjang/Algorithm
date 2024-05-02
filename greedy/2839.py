# ex1 = 18
# ex2 = 4
# ex3 = 6
# ex4 = 9
# ex5 = 11
sugar = int(input())

def delivery(sugar):
    num = 0
    while True:
        if sugar % 5 == 0:
            num += sugar // 5
            print(num)
            break
        num += 1
        sugar -= 3

        if sugar < 0:
            print(-1)
            break
delivery(sugar)
# delivery(ex1)
# delivery(ex2)
# delivery(ex3)
# delivery(ex4)
# delivery(ex5)
