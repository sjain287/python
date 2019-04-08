class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


chick = Chicken()
chick.eat()
chick.fly()  # abused inheritance
