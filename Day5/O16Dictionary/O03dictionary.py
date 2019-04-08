from pprint import pprint

print("_" * 30)
car = {
    "brand": "Mercedez",
    "model": "S600",
    "Year": 1964  # ,
    # "color": "White"
}
# uncomment above code and see the difference
print(car)

x = car.setdefault("color", "blue")
print("x=", x)
print(car)

print("_"*30)
x1 = car.setdefault("color", "Red")
print("x=", x1)
print(car)
print("_"*30)
print("The {brand} of {model} in {Year}".format_map(car))
print("_" * 30)
