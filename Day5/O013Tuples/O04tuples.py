from collections import namedtuple

person = namedtuple("person", "Name age height")
user = person(Name="salman", age=40, height=145)
print(user)

print(user.Name)
print(user.age)
print(user.height)

print("_" * 50)
