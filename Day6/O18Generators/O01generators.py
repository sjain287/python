from sys import getsizeof
# simple comprehension
print([x for x in range(11)])
# this always throws a new data structure
print(sum([x for x in range(11)]))
# generator (ditch square brackets[])- it always yields
# whenever we encounter yield keyword in a function, thats a generator
print(sum(x for x in range(11)))

print("_" * 50)
values = [x * 2 for x in range(100)]
print(values)
print("Size of the list", getsizeof(values))

print("_" * 50)
values = (x * 2 for x in range(100))
print(values)
print("Size of the generator", getsizeof(values))

for i in values:
    print(i, end=" ")
else:
    print
print("Size of the generator", getsizeof(values))
print("_" * 50)


def fun():
    x = 100
    print("Apple")
    yield x
    x = 200
    print("Orange")
    yield x
    x = 300
    print("Banana")
    yield x

    print("Prunes")
    yield 1000


    # return x
val = fun()
print(val)
# print(val)

print(next(val))
print(next(val))
print(next(val))
print(next(val))
print(next(val))  # throws exception, since generator is empty

for itm in fun():
    print("from loop: ", itm)
