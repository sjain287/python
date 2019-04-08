'''
1.int
2.float
3.complex
....
'''

a = 1
b = -1
c = 1.0
d = -1.0
e = +2e3
f = -2e3
g = 3.14j
h = -3.14j
print(type(a), "\t\t", a)
print(type(b), "\t\t", b)
print(type(c), "\t\t", c)
print(type(d), "\t\t", d)
print(type(e), "\t\t", e)
print(type(f), "\t\t", f)
print(type(g), "\t\t", g)
print(type(h), "\t\t", h)

print("_" * 50)
print(max(1, 2, 3))
print(min(1, 2, 3))
a = 100
print("oct({a})\t\t".format(a=a), oct(a))
print("hex({a})\t\t".format(a=a), hex(a))
print("bin({a})\t\t".format(a=a), bin(a))
print(f"bin({a})\t\t", bin(a))   # using interpolation. used format string
print("round(2.7)\t\t".format(a=a), round(2.7))
print("round(2.5)\t\t", round(2.5))
print("round(2.4)\t\t", round(2.4))
print("abs(-2.4)\t\t", abs(-2.4))


print("Types".center(50, "*"))
x = 2 + 6.5
y = 45
z = 4.5
k = a + b
print(x, "\t\t", type(x))
print(y, "\t\t", type(y))
print(z, "\t\t", type(z))
print(k, "\t\t", type(k))

print("Type conversion".center(50, "*"))
a = 100
print(type(a), "\t\t", a)
print(type(float(a)), "\t\t", float(a))
print(type(complex(a)), "\t\t", complex(a))
print(type(bool(a)), "\t\t", bool(a))
a = 10
print(type(bool(a)), "\t\t", bool(a))
a = 0
print(type(bool(a)), "\t\t", bool(a))  # anything other than 0 is true
a = -1
print(type(bool(a)), "\t\t", bool(a))  # anything other than 0 is true
