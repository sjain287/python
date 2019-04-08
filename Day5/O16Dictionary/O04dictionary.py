'''
sequence to a dictionary by from keys
'''
from pprint import pprint
marks = {}.fromkeys(["Maths", "Science", "ComputerScience"])
print(marks)
marks1 = {}.fromkeys(["Maths", "Science", "ComputerScience"], 'Not Set')
print(marks1)
marks2 = {}.fromkeys(["Maths", "Science", "ComputerScience"], 0)
print(marks2)

print("_" * 40)

for itm in marks2.items():
    print(itm)

print("_" * 40)
print(list(sorted(marks2.keys())))
print("_" * 40)
seq = ('name', 'age', 'sex')

d1 = dict.fromkeys(seq)
pprint(d1, width=10)
print("This is a dictionary : %s" % str(d1))

print("_" * 40)
d1 = dict.fromkeys(seq, 100)
pprint(d1, width=10)
print("This is a dictionary : %s" % str(d1))

print("_" * 40)
F = {'a': "apple", 'b': "banana"}
S = {'o': "okra", 'p': "potato"}
T = {'k': 'kangaroo', 'e': 'elephant'}
combine = {**F, **S, **T}
pprint(combine, width=10)
