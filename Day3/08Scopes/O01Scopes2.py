x = "apple"


def call_me():
    print(x)


call_me()

print("_" * 30)


def call_me_again():
    global x
    x += "Ooty"
    print(x)


call_me_again()
print(x)
