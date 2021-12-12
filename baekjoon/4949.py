exam = '''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]). ..
'''
split_exam = exam.split(".")


def analyzer(text):
    stack = []
    state = True
    for str in text:
        if (str == "("):
            stack.append("(")
        if (str == ")"):
            if not (stack) or (stack[-1]) == "[":
                state = False
                break
            if (stack)[-1] == "(":
                stack.pop()
        if (str == "["):
            stack.append("[")
        if (str == "]"):
            if not (stack) or (stack[-1]) == "(":
                state = False
                break
            if (stack[-1]) == "[":
                stack.pop()

    if not stack and state == True:
        print("yes")
    else:
        print("no")


for text in split_exam:
    if (text == ""):
        break
    analyzer(text)

# while True:
#     text = input()
#     if text == ".":
#         break

#     stack = []
#     state = True
#     for str in text:
#         if (str == "("):
#             stack.append("(")
#         if (str == ")"):
#             if not (stack) or (stack[-1]) == "[":
#                 state = False
#                 break
#             if (stack)[-1] == "(":
#                 stack.pop()
#         if (str == "["):
#             stack.append("[")
#         if (str == "]"):
#             if not (stack) or (stack[-1]) == "(":
#                 state = False
#                 break
#             if (stack[-1]) == "[":
#                 stack.pop()

#     if not stack and state == True:
#         print("yes")
#     else:
#         print("no")
