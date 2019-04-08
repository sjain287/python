class Point:
    encoding_technique = "MTOM"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    # def InitMe(cls):
    def Zero(cls):  # static method # factory- method that returns object
        return cls(0, 0)

    def __str__(self):  # object castion to string
        return f"Point Plotted ({self.x},{self.y})"

    def __eq__(self, other):
        print("Custom == called")
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


p1 = Point(114, 242)
p2 = Point(11, 22)
print(id(p1))
print(id(p2))
print(p1 == p2)  # if custom eq is not present it will comapre with object address
print(p1 > p2)
print(p1 < p2)  # python implicitly takes care of it, since we overloaded __gt
