l1 = [11, 22, 33, 44]
l2 = [111, 222, 333, 444]
print(zip(l1, l2))
print(list(zip(l1, l2)))

print(list(zip("ape", l1, l2)))
print(list(zip("apew", l1, l2)))
print(list(zip("ap", l1, l2)))
