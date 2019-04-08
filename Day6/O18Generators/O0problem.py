'''
fibonacci series
1. using function generator
2. class generator
'''


def fib(terms):
    a, b = 0, 1
    for i in range(terms):
        yield a
        a, b = b, a + b


print('Fibonacci using function Generator'.center(80, '*'))
n = 10
x = fib(n)
for i in x:
    print(i, end=" ")
print()

print('Fibonacci using Class Generator'.center(80, '*'))


class fib_class:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        temp = self.a
        self.a, self.b = self.b, self.a + self.b
        return temp


n = 10
x = iter(fib_class())
for i in range(n):
    print(next(x), end=" ")
print()
