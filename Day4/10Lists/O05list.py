l1 = [1, 2, , 3, 4, 5]
l2 = [11, 22, 33, 44, 55]
l3 = [*l1, *l2]
print(l3)

values = ["a", "b", "c", "d"]
print(values)

for ch in values:
    print(ch)

print("_" * 30)
for ch in enumerate(values):
    print(ch)

print("_" * 30)

for ch in enumerate(values):
