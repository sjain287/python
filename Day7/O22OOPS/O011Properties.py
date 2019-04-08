class Person():

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary
        #self.PName = self.__name

    def __str__(self):
        return f"{self.__name},{self.__age},{self.__salary}"

    # method 2
    @property
    def PAge(self):
        return self.__age

    @PAge.setter
    def PAge(self, value):
        self.__age = value

    def setName(self, name):
        self.__name = name

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name
    # method 1
    PName = property(get_name, set_name)

    def set_age(self, value):
        self.__age = value

    def get_age(self):
        return self.__age

    def set_salary(self, value):
        self.__salary = value

    def get_salary(self):
        return self.__salary

    PAge = property(get_age, set_age)
    PSalary = property(get_salary, set_salary)


person = Person("sachin", 45, 45000)
print(person)

salary_info = person.PSalary
age_info = person.PAge
name_info = person.PName
print(name_info)
print(person.get_name())
print("_"*50)
print(age_info)
print("_"*50)
print(salary_info)
print("_"*50)
print(person.PAge)


person.PAge = 78
age = person.PAge

print(person.PAge)
print(age)
