class Animal:
    def __init__(self):
        print("Animal CTor")
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal CTor")
        self.weight = 3

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


anm = Animal()
mam = Mamal()
