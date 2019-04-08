# tuples are immutable
# tuple is read only, but if it comprises list then the list can be changed

# ways to define a tuple
p1 = (1, 2)
p2 = 11, 22
p3 = 12,  # comma is needed else it will be a integer variable
p4 = ()
p5 = tuple()

print(type(p1))
print(type(p2))
print(type(p3))
print(type(p4))
print(type(p5))
print("_" * 50)

x, y = 12, 13
x, y = y, x  # swapping
print(x, y)

print("_" * 50)
p5 = (11, 22) + (10, 20)  # concats tuples
print(p5)
print("_" * 50)
p6 = p1+p2
print(p6)
print("_" * 50)
p7 = (11, 22) * 3
print(p7)
