class Twice_me:
    def __init__(self, upper_limit=0):
        self.upper = upper_limit

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i > self.upper:
            raise StopIteration
        temp = self.i * 2
        self.i += 1
        return temp
    pass


gen = Twice_me(10)
print(gen)
iter(gen)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(type(gen))

print("_"*30)
for n in Twice_me(10):
    print(n)
