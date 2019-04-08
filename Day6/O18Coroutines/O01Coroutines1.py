# opposit to Generator
# Generator- generates data for iteration
# Coroutine - consumes data
# regenerator- ??


def show_detail(greet):
    print(f'Parameter received is {greet}')
    while True:
        name = (yield)
        print("Business Executed")
        if greet in name:
            print(name)


corout = show_detail("Sweet")
print(corout)
corout.__next__()  # will start coroutine execution and advances to first yield

corout.send("Sachin")
corout.send("Sweet Sachin")
corout.send("Sweet Rahul")
corout.send("Sweet Sehwag")
