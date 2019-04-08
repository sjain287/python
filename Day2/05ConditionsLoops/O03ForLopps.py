for num in range(3):
    print(num, "\t", end="")
print()
print("_" * 30)

for num in range(1, 3):
    print(num)
print()
print(num, "\t", end="")

for num in range(1, 10, 2):
    print(num)
print(num, "\t", end="")
print()


for x in range(1, 11):
    if x % 2 == 0:
        print("\t\t\t", x)
    else:
        print("\t\t", x)
