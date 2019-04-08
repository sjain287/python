class preEvaluation:
    """ Prefix Evaluation using class
    """
    @staticmethod
    def prefixEval(prefixExp):
        rev_prefixExp = prefixExp[::-1]
        operandStack = []

        for num in rev_prefixExp:
            if num in "0123456789":
                operandStack.append(int(num))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(num, operand2, operand1)
                operandStack.append(result)
        return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


exp = '++78+32'
pe = preEvaluation()
print(preEvaluation.prefixEval(exp))
