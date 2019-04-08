
# way 1


def compute_hcf(num1, num2):
    if num1 == 0:
        return num2
    else:
        return (compute_hcf(num2 % num1, num1))

# way2


def hcf(n1, n2):
    if (n1 > n2):
        small = 2
    else:
        small = n1
    # using Ternary operator
    # for i in ((n1 if n1 > n2 else n2), 0, -1):
    #     if n1 % i == 0 and n2 % i == 0:
    #         break

    for i in range(small + 1, 0, -1):
        if n1 % i == 0 and n2 % i == 0:
            break
    return i

# way 3


def gcd(n1, n2):
    while (n2 != 0):
        n1, n2 = n2, n1 % n2
    return n1

# way 4


def gcd1(n1, n2):
    return n1 if n2 == 0 else gcd1(n1, n2 % n1)

# way 5


def hcf2(n1, n2):
    while (n1 != n2):
        n1, n2 = (n1-n2, n2) if n1 > n2 else (n2, n2-n1)
        # if (n1 > n2):
        #     n1 -= n2
        # if (n2 > n1):
        #     n2 -= n1
    return n1

# way 6


def hcf3(n1, n2):
    n1, n2 = (n1-n2, n2) if n1 > n2 else (n2, n2-n1)
    return n1 if n1 == n2 else hcf3(n1, n2)


num1 = 17
num2 = 0
print(f"The H.C.F of {num1} and {num2} is {compute_hcf(num1,num2)}")
