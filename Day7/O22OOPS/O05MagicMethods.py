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


p1 = Point(11, 22)
p2 = Point.Zero()
print(p1.__str__())
print(str(p2))
print(p2)
