

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
