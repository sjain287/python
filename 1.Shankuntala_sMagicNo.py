'''
1.
	1=1!
    2=2!
    145=1! + 4! 5!
    Which is next no to follows this concept?  (40585)
'''
import math

success = True
count = 0
start = 1
sum = 0

print("Shakuntala's Magic nos are:\n")
while count <= 4:
    sum = 0
    for i in str(start):
        sum = sum + math.factorial(int(i))
    if (start == sum):
        print(start)
        count = count + 1
    start = start + 1
else:
    print("Success")

print("_"*50)
