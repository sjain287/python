mat = []
print(mat)

for i in range(0, 3):
    mat.append([])
    for j in range(0, 3):
        mat[i].append([0])

print(mat)

for lis in mat:
    for elem in lis:
        print(elem, end="\t")
    print()
