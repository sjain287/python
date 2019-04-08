
# custom generator


def twice_me(upper_limit=0):
    n = 0
    while n < upper_limit:
        yield n * 2
        n += 1


for n in twice_me(10):
    print(n)

'''
1. Easy to implement
2. Mermory efficient
3. infinite stream representation
'''
