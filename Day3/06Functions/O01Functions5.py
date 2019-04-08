# Args
def multiply(*nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod


print(multiply(1, 2, 3, 4, 5))
