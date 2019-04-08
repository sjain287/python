'''
 8 1 6
 3 5 7
 4 9 2
create a magic matrix whose sum of rows and colums will be same
Algo:
1. start from mid column of top row
2. if curr pos is top row ==> 
go to  bottom row+1 column
3. if right most column ==> f
go to first column -1 row
4. if right top diagonal is free then fill it
5. if no options 1 row down


'''

m = 5
f = 1
l = f + m * m - 1
sum = (f + l) / 2 * m
start_pos = m // 2 + 1
mat = []
print(f"sum of all sides ={sum}")
for i in range(0, m):
    mat.append([])
    for j in range(0, m):
        mat[i].append(0)

# print(mat)
# ---------------------------------------------------------------------
i, j = 0, m // 2
while (f <= l):
    mat[i][j] = f
    f += 1
    if (i == 0 and j != m-1):
        i, j = m - 1, j + 1
    elif (j == m - 1 and i != 0):
        i, j = i - 1, 0
    elif (i != 0 and j != m - 1 and mat[i - 1][j + 1] == 0):
        i, j = i - 1, j + 1
    else:
        i += 1

for lis in mat:
    for elem in lis:
        print(elem, end="\t")
    print()

# print(mat[1][0])
