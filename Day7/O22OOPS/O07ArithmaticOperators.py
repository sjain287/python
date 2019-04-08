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

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Point(self.x // other.x, self.y // other.y)


p1 = Point(10, 20)
p2 = Point(2, 5)

print(p1)
print(p2)

p3 = p1+p2
p4 = p1-p2
p5 = p1*p2
p6 = p1/p2
p7 = p1 // p2

print(p3)
print(p4)
print(p5)
print(p6)
print(p7)
