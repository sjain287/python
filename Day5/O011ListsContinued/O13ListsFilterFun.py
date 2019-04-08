import pprint
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
#pprint.pprint(items, indent=2)
print("_" * 40)
'''
filter : Return an iterator yielding those items of iterable for which function(item) is true. 
If function is None, return the items that are true.
simply filters based on the condition
'''
fil = list(filter(lambda items: items[1] < 501, items))
pprint.pprint(fil, indent=2)
