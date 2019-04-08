
# named tuples
from collections import namedtuple


def math_opr(x, y):
    add = x + y
    mul = x * y
    quotient = x // y
    diff = x - y
    res = namedtuple("result", "Addition Multiply Quotient Difference")
    actual_result = res(add, mul, quotient, diff)
    return actual_result


print(math_opr(40, 10))
calc = math_opr(44, 10)
print(calc.Addition)
