class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mamal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


anm = Animal()
mam = Mamal()
mam.eat()
mam.walk()

print('_' * 50)
fish = Fish()
fish.eat()
fish.swim()
print('_' * 50)

print(isinstance(mam, Mamal))
print(isinstance(mam, Animal))
print(isinstance(mam, object))
print(isinstance(mam, Fish))
print('_' * 50)

print(issubclass(Mamal, Animal))
print(issubclass(Mamal, object))
