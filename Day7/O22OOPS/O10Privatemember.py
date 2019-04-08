class Student:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    @classmethod
    def StudentFactory(cls, id, name, age):
        print("Student factory called ")
        return cls(id, name, age)

    def __str__(self):
        return f"id={self.id} name={self.name} age={self.age}"


naman = Student.StudentFactory(101, "sachin", 45)

print(naman.__dict__)

print(naman.age)
print(naman.name)
print(naman.id)
