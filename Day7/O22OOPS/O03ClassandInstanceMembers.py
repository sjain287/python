class Point:
    encoding_technique = "MTOM"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Plot(self):
        print(f"Point Plotted ({self.x},{self.y})")


p1 = Point(10, 20)
p2 = Point(11, 22)

print(p1.x, p2.y)

p2.z = 33  # Python objects are implicitly Expandos
# Expandos are those objects for which we can keep appending values

print("p2=", p2.x, p2.y, p2.z)

p1.Plot()
p2.Plot()

print("_" * 50)
#p1.encoding_technique = "binary"
print(p1.encoding_technique)
print(p2.encoding_technique)
print(Point.encoding_technique)

print("_" * 50)
p1.encoding_technique = "binary"
p2.encoding_technique = "xml"  # these works as expando
print(p1.encoding_technique)
print(p2.encoding_technique)
print(Point.encoding_technique)

print("_" * 50)
Point.encoding_technique = "binary"
#p2.encoding_technique = "xml"
print(p1.encoding_technique)
print(p2.encoding_technique)
print(Point.encoding_technique)
