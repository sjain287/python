abc = [(x, y) for x in range(5) for y in range(5)]
print(abc)
print("_"*50)
abc = [(x, y) for x in range(5) for y in range(x+1)]
print(abc)
print("_"*50)
