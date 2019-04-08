'''
A+b=ab+
A+b*c+d
=a+[bc*]+d
=[abc*+]+d
=abc*+d+
infix to postfix
A+b*(x+y*z+k)+e^f+c*m-n
=a+b*(x+(yz*+k)+e^f+c*m-n
=a+((xyz*+)+k)+e^f+c*m-n
=....
=....
=abxyz*+k+*ef^+cm*+n-
'''


def chk_idx(chr):
    opList = ["^", ["*", "/"], ["+", "-"], ["(", ")"]]
    for i in range(len(opList)):
        temp = opList[i]
        if chr in temp:
            ret = i + 1
            break
    else:
        ret = 0
    return ret


infixexpr = "A+b*(x+y*z+k)+e^f+c*m-n"
'''
=abxyz*+k+*ef^+cm*+n-
'''
#infixexpr = "A+b*c+d"
opStack = []
postfixList = []
for elem in infixexpr:
    if chk_idx(elem) == 0:
        postfixList.append(elem)
    elif elem == '(':
        opStack.append(elem)
    elif (len(opStack) != 0 and opStack[-1] == '('):
        opStack.append(elem)
    elif elem == ')':
        topelem = opStack.pop()
        while topelem != '(':
            postfixList.append(topelem)
            topelem = opStack.pop()
    elif len(opStack) == 0:
        opStack.append(elem)
        # continue
    else:
        while len(opStack) != 0 and (chk_idx(opStack[-1]) <= chk_idx(elem)):
            temp = opStack.pop()
            postfixList.append(temp)
        opStack.append(elem)

while len(opStack) != 0:
    temp = opStack.pop()
    postfixList.append(temp)
for i in postfixList:
    print(i, end="")
