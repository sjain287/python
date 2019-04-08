
print("_" * 40)
print("{item:30}\t{Price:50}".format(item="Item", Price="Price"))
print("=" * 40)
print("{item:30}\t{Price:4}".format(item="Apples", Price="0.4"))
print("{item:30}\t{Price:4}".format(item="Pears", Price="0.5"))
print("{item:30}\t{Price:4}".format(item="Appricots", Price="1.92"))
print("{item:30}\t{Price:4}".format(item="Prunes", Price="12"))
print("{item:30}\t{Price:4}".format(item="Cashew", Price="20"))
print("{item:30}\t{Price:4}".format(item="Dates", Price="15"))

print("_" * 40)

print("\n\nAlternate way using formats\n")
# alternate way
width = 60
price_width = 10
item_width = width - price_width
header = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)
print("_"*width)
print(header.format('Item', 'Price'))
print("=" * width)
print(fmt.format("Apples", 0.4))
print(fmt.format("Pears", 0.5))
print(fmt.format("Appricots", 1.92))
print(fmt.format("Prunes", 12))
print(fmt.format("Cashew", 20))
print(fmt.format("Dates", 15))
print("_"*width)
print(header)
print(fmt)
