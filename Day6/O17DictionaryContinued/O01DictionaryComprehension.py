d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(d1)
print(d1.keys())
print(d1.values())
print(d1.items())

d2 = {k: v for (k, v) in d1.items()}
print(d2)
print("_"*50)
d2 = {k: v**2 for (k, v) in d1.items()}
print(d2)
print("_"*50)

d2 = {k*2: v*2 for (k, v) in d1.items()}
print(d2)
print("_" * 50)

keys = ['a', 'b', 'c', 'd', 'e']
Values = [1, 2, 3, 4, 5]

d2 = dict(zip(keys, Values))
print(d2)
print("_" * 50)

d4 = {k: v ** 2 for (k, v) in zip(keys, Values)}
print(d4)
print("_" * 50)

d5 = {i: i**2 for i in range(16)}
print(d5)
print("_" * 50)

d6 = {i: i**2 for i in range(16) if i % 2 == 0}
print(d6)
print("_" * 50)

d7 = {i: i**2 for i in range(21) if i % 2 == 0 if i % 5 == 0}
print(d7)
print("_" * 50)
