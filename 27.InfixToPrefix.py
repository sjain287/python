def Precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    if ch == '*' or ch == '/':
        return 2
    if ch == '^':
        return 3
    else:
        return 0


def Push(lst, elem):
    lst.append(elem)


def Pop(lst):
    return lst.pop()


def Disp(lst):
    for i in reversed(lst):
        print(i, end="")


def Rev(exp):
    return exp[::-1]


class InToPre:

    @staticmethod
    def InToPre(InfixExp):
        acceptedCharset = 'abcdefghijklmnopqrstuvwxyz'
        opStack = []
        prefixExp = []
        revInfix = Rev(InfixExp)
        for elem in revInfix:
            if elem in acceptedCharset:
                Push(prefixExp, elem)
            elif elem == ')':
                Push(opStack, elem)
            elif elem == '(':
                topelem = Pop(opStack)
                while topelem != ')':
                    Push(prefixExp, topelem)
                    topelem = Pop(opStack)
            elif len(opStack) == 0:
                Push(opStack, elem)
            else:
                while (len(opStack) != 0) and (Precedence(opStack[-1]) > Precedence(elem)):
                    Push(prefixExp, Pop(opStack))
                Push(opStack, elem)

        while len(opStack) != 0:
            temp = opStack.pop()
            Push(prefixExp, temp)
        # print(prefixExp)
        Disp(prefixExp)


InfixExp = 'a+b*c+d'
InfixExp = 'a+b*(x+y*z+k)+e^f+c*m-n'
InToPre.InToPre(InfixExp)
