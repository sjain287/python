# nested function
def fun1(msg):
    msg = msg
    print("Hello")

    def inner():
        print(msg)

    print("Hi")
    print("Haaaaaaaaaaa")
    return inner   # higher order functions accepts a function or returns a function


in_fun = fun1("Election nearing")  # storing Function o/p (the return function)
in_fun()  # callback

# Closure is nothing but which remebers parent's content for callback
