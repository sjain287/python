'''
union
intersection
difference
symmetric difference
'''

print("_" * 50)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union
print("union".center(40, '*'))
print("Set A", A)
print("Set B", B)
print(A.union(B))
print(B.union(A))
print(A | B)

# Intersection
print("Intersection".center(40, '*'))
print("Set A", A)
print("Set B", B)
print(A.intersection(B))
print(B.intersection(A))
print(A & B)

# difference
print("difference".center(40, '*'))
print("Set A", A)
print("Set B", B)
print(A.difference(B))
print(A - B)
print(B.difference(A))
print(B - A)

# Symmetric difference
print("Symmetric difference".center(40, '*'))
print("Set A", A)
print("Set B", B)
print(A.symmetric_difference(B))
print(A ^ B)
print(B.symmetric_difference(A))
print(B ^ A)

# in- not in
print("In-not In".center(40, '*'))
my_set = set("apple")
print('a' in my_set)
print('p' not in my_set)

# set is iterable
for i in my_set:
    print(i)

my_set.clear()
print(my_set)
