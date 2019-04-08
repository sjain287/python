class Employee:
    def __init__(self):
        print("Employee Ctor")
        self.name = "Sachin"

    def greet(self):
        print("greet employee")


class Person:
    def __init__(self):
        print("Person CTOR")
        self.age = 45

    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    def __init__(self):
        Employee.__init__(self)
        Person.__init__(self)
        print("Manager CTor")
        self.projID = 101

    def greet(self):
        print("Manager greet")


man = Manager()
man.greet()
print("_" * 50)

print(man.name)
# print(man.age())
# print(man.projID())
