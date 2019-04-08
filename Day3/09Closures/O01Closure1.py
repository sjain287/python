# nested function
def fun1(msg):
    msg = msg
    print("Hello")

    def inner():
        print(msg)

    print("Hi")
    inner()
    print("Haaaaaaaaaaa")


fun1("Election nearing")
