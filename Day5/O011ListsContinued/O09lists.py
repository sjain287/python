values = ["a", "b", "c", "d"]
# index function
print(values.index("a"))
print(values.index("c"))

# in operator
print("Apple" if "c" in values else "Orange")
print("Apple" if "e" in values else "Orange")

if "x" in values:
    print("CSK")
else:
    print("RCB")

# counts occurances of given element
print(values.count('b'))
print(values.count('a'))
