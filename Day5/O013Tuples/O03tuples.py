t = ("Banana", [5, 8, 10])
print(t)
print(t.index("Banana"))
print(t[0])
print(t[1])
t[1].append(15)
print(t[1])
print("_" * 80)

tup = (101, 102, ["Deepika", "Aishwarya", "Genelia", "Juhi Chawla"])
tup[2][2] = "Deshmukh"
print(tup)
print("_" * 80)
del tup  # delete a tuple
print(tup)
