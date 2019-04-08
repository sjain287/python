# modules
import cmath  # for complex mathematics
from math import sqrt  # square root function
import random
import math
print("Random No between 0.0 and 1".center(50, "*"))
print(random.random())
print("Random No between 1 and 100".center(50, "*"))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))
print("chose a no from a list".center(50, "*"))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("chose a sample from a list".center(50, "*"))
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))

# choices is similar to sample but the difference is choices allows list with replacement but sample doesnt
print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 2)

print("Math Functions".center(50, "*"))
print("Ceil(2.4", math.ceil(2.4))
print("Fact(5)", math.factorial(5))
print("Floor(2.7)", math.floor)
print("sqrt(4)", sqrt(4))

# Dealing with complex mathematics
print(cmath.sqrt(-1))
print((1+3j)*(2+5j))
