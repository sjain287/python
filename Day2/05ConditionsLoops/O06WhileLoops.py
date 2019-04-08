num = 346
sum = 0
while num > 0:
    sum = sum * 10 + num % 10
    num //= 10

print(f"Reverse is {sum}")

print("_" * 50)

x, y = 50, 15
while x != y:
    if (x > y):
        x -= y
    if (y > x):
        y -= x
else:
    print("Job done")

print(f"HCF is {x}")

print("_" * 50)
