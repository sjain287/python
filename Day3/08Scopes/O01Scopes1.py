def fun():
    x, y = 12, 13  # local variables
    print(f'x={x} y={y}')


fun()


def fun1(name):  # local variable
    print(name)


fun1("Sachin")


def fun2():
    print(msg)


msg = "SRH won against RR"  # Global Variable
fun2()


def fun3():
    global msg  # calling Global variable
    msg = msg + '!!!'
    print(msg)


fun3()
