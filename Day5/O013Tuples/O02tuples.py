l1 = [1, 2, 3]
p1 = tuple(l1)
print(p1)


p8 = tuple("sachin")
print(p8)

print(p8[0:2])
print(p8[0:5])
print(p8[0:5:2])
print(p8[2:-2])
print(p8[-2])
print("_" * 50)
x, *y, z = p8
print(x, y, z)

# in operator in tuple
print("_"*50)
if 'a' in p8:
    print("Apple")
else:
    print("Orange")

print("_" * 50)
# not in operator in tuple
if 'z' not in p8:
    print("Prunes")
else:
    print("Apricot")
