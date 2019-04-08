class Animal:
    def eat(self):
        print("Eat")


class Bird(Animal):
    def fly(self):
        print("Fly")


class Chicken(Bird):
    pass


chick = Chicken()
chick.eat()
chick.fly()
