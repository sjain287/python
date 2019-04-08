import pprint
items = [
    ("FCC", 200),
    ("face powder", 800),
    ("blue eye liner", 500),
    ("eye brow comb", 250),
    ("lipstick", 100),
    ("foundation", 500)
]

# comprehension
# variable=[expression for item in items]
prices = [item[1] for item in items]
print(prices)
print("_" * 40)

new_items = [item for item in items if item[1] < 501]
pprint.pprint(new_items, indent=True)
print("_" * 40)
