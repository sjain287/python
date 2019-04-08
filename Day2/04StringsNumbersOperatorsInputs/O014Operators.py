'''
    Arithmatic Operators
    COmparison Operators
    Logical
    Assignment
    Bitwise
    Ternary(conditional)
'''

print(10+3)
print(10-3)
print(10*3)
print(10/3)
print(10//3)
print(10 % 3)
print(10+3)
print(10 ** 3)
print("_"*50)
# augmentors operators
x = 10
x += 3
x //= 3
x *= 3
x **= 3
print(f"x={x}")
print("_"*50)
'''
==
!=
<
>
<=
>=
'''
print("_"*50)
# comparison operators
print(1 == 1)
print(1 == 2)
print(1 != 2)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)

print("_"*50)
# logical operators
'''
AND
OR
NOT
'''

print(1 == 1 and 2 == 2)
print(1 == 2 or 2 == 2)
print(not 1 == 1)

print("_"*50)
print("apple" > "orange")  # works on ordinal value
print(ord("a"))
print(ord("o"))

print("_"*50)
print("Bitwise operators ( | & ^ << >> ~)".center(50, "*"))
print(5 | 6)
print(5 & 6)
print(5 ^ 6)
print("_"*50)
print(3 << 2)
print(5 << 1)
print(5 >> 2)
print(6 << 1)
# ternary operator
a = 7
print("Apple" if a < 10 else "Orange")
print("Apple" if a > 10 else "Orange")
msg = "Plays" if a > 13 else "Doesn't Play"
print(msg)
