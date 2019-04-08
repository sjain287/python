my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for lis in enumerate(my_list):
    print(lis)
print("_" * 50)

for index, lis in enumerate(my_list):
    print(index, lis)

print("_" * 50)

for l1 in my_list:
    for elem in l1:
        print(elem, end=" ")
    print()

print("_" * 50)
for ind1, l1 in enumerate(my_list):
    for ind2, elem in enumerate(l1):
        print(elem, end=" ")
    print()
