def fun(info):
    info_len = len(info)
    for i in range(info_len - 1, -1, -1):
        yield info[i]


for ch in fun("naman"):
    print(ch, end="")
print()
for ch in fun("naman"):
    print(ch, end="")
