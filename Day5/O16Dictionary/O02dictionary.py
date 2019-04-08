from pprint import pprint
# {}
d1 = {"fname": "John", "lname": "Taylor"}
# dict()
d2 = dict({"mining": "BGML", "Place": "KGF"})
# sequence of pairs
d3 = ([(1, "apple"), (2, "orange"), (3, "Pine")])
# key value pairs
d4 = dict(saif="Kareena", Ranveer="Deepika", Ranbir="Alia")

pprint(d1, width=10)
print("_"*30)
pprint(d2, width=10)
print("_"*30)
pprint(d3, width=10)
print("_" * 30)
print(d4["saif"])
print("_" * 30)
print(d4.get("Ranbir"))
print("_" * 30)
# accessing non existing key
# print(d4["Salman"])
# print(d4.get("Salman"))


# update value in the dictionary
d4["saif"] = "Amrita"
pprint(d4, width=10)
print("_" * 30)

d4.pop("saif")
pprint(d4, width=10)
print("_" * 30)

d5 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
pprint(d5, width=10)
print("_" * 30)
d5.pop(3)
pprint(d5, width=10)
print("_" * 30)
print(f'popitem(){d5.popitem()}')
pprint(d5, width=10)
print("_" * 30)
del d5[1]
pprint(d5, width=10)
print("_" * 30)

d5.clear()
pprint(d5, width=10)
print("_" * 30)
del d5
# uncomment will give error. since d5 doesn't exist in memory
# pprint(d5, width=10)
print("_" * 30)
