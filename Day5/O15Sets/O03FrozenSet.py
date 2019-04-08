# a frozen set is a immutable set
# it is read-only

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
print(A.isdisjoint(B))
print(A.difference(B))
print(A | B)

# methods like pop, discard remove clear etc are not available
