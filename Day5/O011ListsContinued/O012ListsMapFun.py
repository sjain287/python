import pprint
# list of complex type

items = [
    ("FCC", 200),
    ("face powder", 800),
    ("blue eye liner", 500),
    ("eye brow comb", 250),
    ("lipstick", 100),
    ("foundation", 500)
]
# formating o/p of list using PrettyPrint
# print(items)
pprint.pprint(items, indent=2)
print("_" * 40)

#
prices = []
for item in items:
    prices.append(item[1])
print(prices)
print("_" * 40)


def funDBDA(itm):
    return itm[1]


# map converts one schema to other
pricesNew = map(funDBDA, items)
print(pricesNew)
print("_" * 40)
for it in pricesNew:
    print(it, end="")
print()
print("_" * 40)
# lambda is short form of function
# lambda could be used as closure, but it's not a closure
pricesNew1 = map(lambda comodity: comodity[1], items)
print(pricesNew1)
print("_" * 40)
for it in pricesNew1:
    print(it, end="")
print()


print("_" * 40)
pricesNew1 = list(map(lambda comodity: comodity[1], items))
print(pricesNew1)
