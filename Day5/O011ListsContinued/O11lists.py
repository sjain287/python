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
print(items)
pprint.pprint(items, indent=2)
print("_" * 40)
items.sort()
print("_" * 40)
pprint.pprint(items, indent=2)
print("_" * 40)


def sort_item():
    return items[1]


items.sort(key=sort_item)
pprint.pprint(items, indent=2)
print("_" * 40)

items.sort(key=sort_item, reverse=True)
pprint.pprint(items, indent=2)
print("_" * 40)

# use of lambda
items.sort(key=lambda items: items[0], reverse=True)
pprint.pprint(items, indent=2)
print("_" * 40)
