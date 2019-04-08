from pprint import pprint
d1 = {k: v for (k, v) in zip(
    (chr(x) for x in range(97, 123)), (n for n in range(1, 27)))}
print(d1)

d2 = list(range(11))
print(d1)

d2 = {k: ('Even' if k % 2 == 0 else 'Odd') for k in list(range(11))}
pprint(d2, indent=True)
