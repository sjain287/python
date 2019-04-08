class Point:
    encoding_technique = "MTOM"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    # def InitMe(cls):
    def Zero(cls):  # static method # factory- method that returns object
        return cls(0, 0)

    def Plot(self):
        print(f"Point Plotted ({self.x},{self.y})")


p1 = Point(11, 22)
p2 = Point.Zero()
p1.Plot()
p2.Plot()
